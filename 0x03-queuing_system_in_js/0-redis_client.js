import redis from 'redis'


const client = redis.createClient();


client.on('connect', () => {
	console.log('Redis client connected to the server');
});

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error.message}`)
});

// Close the Redis connection when the script finishes running
process.on('SIGINT', () => {
	client.quit();
});

// Keep the script running for a while to allow connecting and logging messages
setTimeout(() => {
	client.quit();
},5000);
