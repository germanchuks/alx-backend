import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '2348068638310',
  message: 'This is the code to verify your account.'
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) return;
    console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});