import { createClient } from 'redis';


const client = createClient();

client.on('connect', () => {

  console.log('Redis client conneted to the server');
  
  client.subscribe('Holberton school channel');
});

client.on('error', err => {

  console.log('Redis client not connected to the server', err);
});

client.on('message', (channel, message) => {

  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('Holberton school channel');
    client.quit();
  }
});
