import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;

const redisClient = redis.createClient();
const setAsync = promisify(redisClient.set).bind(redisClient);
const getAsync = promisify(redisClient.get).bind(redisClient);


const queue = kue.createQueue();

// Reserve initial seats
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

// Get current available seats
const getCurrentAvailableSeats = async () => {
  const numberOfAvailableSeats = await getAsync('available_seats');
  return numberOfAvailableSeats;
};

// Initialize available seats to 50
reserveSeat(50);

// Initialize reservation status
let reservationEnabled = true;

// Route: GET /available_seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

// Route: GET /reserve_seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: "Reservation are blocked" });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: "Reservation failed" });
    } else {
      res.json({ status: "Reservation in process" });
    }
  });

  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

// Route: GET /process
app.get('/process', async (req, res) => {
  res.json({ status: "Queue processing" });

  queue.process('reserve_seat', async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    availableSeats = parseInt(availableSeats);

    if (availableSeats <= 0) {
      reservationEnabled = false;
      done(new Error("Not enough seats available"));
      return;
    }

    availableSeats--;
    await reserveSeat(availableSeats);

    if (availableSeats === 0) {
      reservationEnabled = false;
    }

    done();
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
