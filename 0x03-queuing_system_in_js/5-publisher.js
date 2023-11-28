import redis from 'redis';

const publisherClient = redis.createClient();

publisherClient.on('connet', () => {
	console.log('Redis client connected to the server');
});

publisherClient.on('error', (error) => {
	console.log(`Redis client not connected to server: ${error.message}`);
});

function publishMessage(message, time) {
	setTimeout(() => {
		console.log(`About to send ${message}`);
		publisherClient.publish('Holberton school channel', message);
	}, time);
}

// Publish message
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton student #3 starts course", 400);
