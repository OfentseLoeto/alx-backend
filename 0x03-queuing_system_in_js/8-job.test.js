import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

beforeEach(() => {
  queue.testMode.enter();
});

afterEach(() => {
  queue.testMode.clear();
  queue.testMode.exit();
});

describe('createPushNotificationsJobs function', () => {
  it('should throw an error if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs('not an array', queue);
    }).toThrow('Jobs is not an array');
  });

  it('should add jobs to the queue', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(list, queue);

    expect(queue.testMode.jobs.length).toEqual(2);
    expect(queue.testMode.jobs[0].type).toEqual('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).toEqual('push_notification_code_3');
  });

  it('should process jobs', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(list, queue);

    queue.testMode.jobs.forEach(job => {
      job.remove();
    });

    expect(queue.testMode.jobs.length).toEqual(0);
  });
});
