import redis from 'redis';


const subscriberClient = redis.createClient();

subscriberClient.on('connect', ()  => {
	console.log('Redis client connected to the server');
});

subscriberClient.on('error', (error) => {
	console.log(`Redis client not connected to the server:, ${error.message}`);
});

subscriberClient.subscribe('Holberton school channel');

subscriberClient.on('message', (channel, message) => {
	console.log(`Message received on channel, ${channel}: ${message}`);

	if (message === 'KILL_SERVER') {
		subscriberClient.unsubscribe();
		subscriberClient.quit();
	}
});
