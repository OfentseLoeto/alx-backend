const kue = require('kue'),


      pushNotificationQueue = kue.createQueue();

// Creating an object containing the job data
const jobData = {
	phoneNumber: '4153518780',
	message: 'This is the code to verify your account',
};

// Create a job with the object created before
const notificationJob = pushNotificationQueue.create('Push_notification', jobData);

// When notifiation job is created without error
notificationJob.on('enqueue', () => {
	console.log(`Notification job created: ${notificationJob.id}`);
});

// Save the job to the queue
notificationJob.save((err) => {
	if (err) throw err;
	console.log(`Job ${notificationJob.id} saved to the queue`);
});

console.log('Queue a new job!');
