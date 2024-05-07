import { createClient } from 'redis';
import redis from 'redis';


const client = createClient();

client.on('connect', () => {

  console.log('Redis client connected to the server');
});

client.on('error', err => {

  console.log('Redis client not connected to the server:', err);
});


client.hset(
  'HolbertonSchool',
  'Poland',
  50,
  redis.print
);

client.hset(
  'HolbertonSchool',
  'Seattle',
  80,
  redis.print
);

client.hset(
  'HolbertonSchool',
  'New York',
  20,
  redis.print
);

client.hset(
  'HolbertonSchool',
  'Bogota',
  20,
  redis.print
);

client.hset(
  'HolbertonSchool',
  'Cali',
  40,
  redis.print
);

client.hset(
  'HolbertonSchool',
  'Peris',
  2,
  redis.print
);


client.hgetall('HolbertonSchool', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log(reply)
  }
});
