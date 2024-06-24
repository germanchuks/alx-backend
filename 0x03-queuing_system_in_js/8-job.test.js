import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {

  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
  });
});