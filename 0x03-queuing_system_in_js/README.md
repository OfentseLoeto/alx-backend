0- queuing system in js
1- Install node_redis using npm

.Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:

.It should log to the console the message Redis client connected to the server when the connection to Redis works correctly
.It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work
Requirements:

To import the library, you need to use the keyword import

2-In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).

Add two functions:

setNewSchool:
.It accepts two arguments schoolName, and value.
.It should set in Redis the value for the key schoolName
.It should display a confirmation message using redis.print
.displaySchoolValue:
.It accepts one argument schoolName.
.It should log to the console the value for the key passed as argument

At the end of the file, call:

.displaySchoolValue('Holberton');
.setNewSchool('HolbertonSanFrancisco', '100');
.displaySchoolValue('HolbertonSanFrancisco');
Requirements:

Use callbacks for any of the operation, we will look at async operations later

3-In a file 2-redis_op_async.js, let’s copy the code from the previous exercise (1-redis_op.js)

.Using promisify, modify the function displaySchoolValue to use ES6 async / await

Same result as 1-redis_op.js
