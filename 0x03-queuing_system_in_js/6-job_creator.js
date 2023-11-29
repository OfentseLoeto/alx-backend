const kue = require('kue');
const queue = kue.createQueue();

// Creating an object containing the job data
const jobData = {
	phoneNumber: '1234567890',
	message: 'Hello, this is a notification!',
};

// Creating a queue named push_notification_code
const pushNotificationQueue = kue.createQueue();

// Create a job with the object created befor
const notificationJob = pushNotificationQueue.create('Push_notification', jobData);

// When notifiation job is created without error
notificationJob.on('enqueue', () => {
	console.log(`Notification job created: ${notificationJob.id}`);
});

// When the job is completed
notificationJob.on('complete', () => {
	console.log('Notification job completed');
	// Remove completed job from Redis
	notificationJob.remove((error) => {
		if (err) throw error;
		console.log(`Removed completed job ${notificationJob.id} from Redis`);

		// Quit the queue
		kue.Shutdown();
	});
});

// When the job is failing
notificationJob.on('failed', (errorMessage) => {
	console.log(`Notification job failed: ${errorMessage}`);
	notificationJob.remove((error) => {
		if (err) throw error;
		console.log(`Remove faild job ${notificationJop.id} from Redis`);

		// Quit the queue
		kue.Shutdown();
	});
});

// Save the job to the queue
notificationJob.save((err) => {
	if (err) throw err;
	console.log(`Job ${notificationJob.id} saved to the queue`);
});

// Start the queue processing
pushNotificationQueue.process('push_notification', (job, done) => {
	// simulate job processing
	console.log(`Processing job {job.id}`);

	// Simulate successfull completion
	done();
});
