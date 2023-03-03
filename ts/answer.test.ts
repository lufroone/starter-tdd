import getAnswer from './answer'
import test from 'tape'

test('it works', t => {
    const res = getAnswer();
    t.equal(res, 42);
    t.end();
})