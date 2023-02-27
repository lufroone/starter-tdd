const answer = require('./index');
const test = require('tape');

test('it works', t => {
    const res = answer();
    t.equal(res, 42);
    t.end();
})