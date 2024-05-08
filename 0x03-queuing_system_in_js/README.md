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

4-In a file named 5-subscriber.js, create a redis client:

.On connect, it should log the message Redis client connected to the server
.On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
.It should subscribe to the channel holberton school channel
.When it receives message on the channel holberton school channel, it should log the message to the console
.When the message is KILL_SERVER, it should unsubscribe and quit


In a file named 5-publisher.js, create a redis client:

.On connect, it should log the message Redis client connected to the server
.On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
.Write a function named publishMessage:
.It will take two arguments: message (string), and time (integer - in ms)

After time millisecond:
  -The function should log to the console About to send MESSAGE
  -The function should publish to the channel holberton school channel, the message passed in argument after the time passed in arguments
At the end of the file, call:


5-In a file named 6-job_creator.js:

Create a queue with Kue

Create an object containing the Job data with the following format:
{
  phoneNumber: string,
  message: string,
}

.Create a queue named push_notification_code, and create a job with the object created before
.When the job is created without error, log to the console Notification job created: JOB ID
.When the job is completed, log to the console Notification job completed
.When the job is failing, log to the console Notification job failed

6-In a file named 6-job_processor.js:

Create a queue with Kue
.Create a function named sendNotification:
.It will take two arguments phoneNumber and message
.It will log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE
.Write the queue process that will listen to new jobs on push_notification_code:
.Every new job should call the sendNotification function with the phone number and the message contained within the job data

Requirements:

.You only need one Redis server to execute the program
.You will need to have two node processes to run each script at the same time
.You muse use Kue to set up the queue

7-In a file named 7-job_creator.js:

Create an array jobs with the following data inside:

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

After this array created:

Create a queue with Kue

.Write a loop that will go through the array jobs and for each object:
.Create a new job to the queue push_notification_code_2 with the current object
.If there is no error, log to the console Notification job created: JOB_ID
.On the job completion, log to the console Notification job JOB_ID completed
.On the job failure, log to the console Notification job JOB_ID failed: ERROR
.On the job progress, log to the console Notification job JOB_ID PERCENTAGE% complete

