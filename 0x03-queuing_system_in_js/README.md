Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - https://redis.io/download/):

$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
Start Redis in the background with src/redis-server
$ src/redis-server &
Make sure that the server is working with a ping src/redis-cli ping
PONG
Using the Redis client again, set the value School for the key Holberton
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
Kill the server with the process id of the redis-server (hint: use ps and grep)
$ kill [PID_OF_Redis_Server]
Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.

Requirements:

Running get Holberton in the client, should return School

1-Install node_redis using npm

Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:

It should log to the console the message Redis client connected to the server when the connection to Redis works correctly
It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work
Requirements:

To import the library, you need to use the keyword import
