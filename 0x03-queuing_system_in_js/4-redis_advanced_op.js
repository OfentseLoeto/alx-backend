import redis from 'redis';

const client = redis.createClient();
client.on('connect', () => {
	console.log('Redis client connected to the server');
});

// Create a hash
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Peris', 2, redis.print);

client.hgetall('HolbertonSchools', (err, reply) => {
	if (err) {
		console.log(`Error getting hash: ${err.message}`);
	} else {
		console.log(reply);

		// Close redis connection when the script finishes running
		client.quit();
	}

});
