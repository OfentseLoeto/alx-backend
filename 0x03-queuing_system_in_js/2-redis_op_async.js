import redis from 'redis';
import { promisify } from 'util';


const client = redis.createClient();
const promisifiedGet = promisify(client.get).bind(client);
const promisifiedSet = promisify(client.set).bind(client);

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error.message}`)
});

// Function to set new school in redis
async function setNewSchool(schoolName, value) {
        await promisifiedSet(schoolName, value);
}

async function displaySchoolValue(schoolName) {
	try {
		const value = await promisifiedGet(schoolName);
		console.log(value);
	} catch (err) {
		console.error(`Error getting value for ${schoolName}: ${err.message}`);
	}
}

// Set and display values
async function main() {
	await setNewSchool('Holberton', 'School');
	await displaySchoolValue('Holberton');
	console.log(`Reply: OK`);

	await setNewSchool('HolbertonSanFancisco', '100');
	await displaySchoolValue('HolbertonSanFrancisco');

	client.quit();
}


main();
