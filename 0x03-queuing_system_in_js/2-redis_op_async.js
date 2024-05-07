import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {

  console.log('Redis client connected to the server');
});

client.on('error', err => {
  console.log('Redis client not connected to thr server', err);
});


const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {

  setAsync(schoolName, value)
    .then(reply => console.log('Reply:', reply))
    .catch(err => console.log(err));
};


const displaySchoolValue = async (schoolName) => {

  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.log(err);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
