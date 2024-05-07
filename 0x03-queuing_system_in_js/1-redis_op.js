import { createClient } from 'redis';
import redis from 'redis';


const client = createClient();

  client.on('connect', () => {
    console.log('Redis client connected to the server');
  });

  client.on('error', err => {
    console.log('Redis client not connected to the server:', err);
  });

function setNewSchool(schoolName, value) {

  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.log(err);
    } else {
      console.log('Reply:', reply);
    }
  });
};

function displaySchoolValue(schoolName) {

  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(err);
    } else {
      console.log(reply);
    }
  });

};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
