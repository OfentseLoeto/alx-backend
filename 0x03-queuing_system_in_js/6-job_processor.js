const kue = require('kue');

const pushNotificationQueue = kue.createQueue();

// Creating a function send a notification
function sendNotification(phoneNumber, message) {
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Queue process to listen to new jobs on push_notification_code
pushNotificationQueue.process('push_notification', (job, done) => {
	// Getting phone number and message from the job
	const { phoneNumber, message } = job.data;

	// Calling the notification function with phone Number and message
	sendNotification(phoneNumber, message);

	// Simulate successful completion
	done();
});

console.log('Job processer is listening for new jobs...');
