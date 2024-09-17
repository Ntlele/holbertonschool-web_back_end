// 0-console.test.js

const { displayMessage } = require('./0-console');
const assert = require('assert');

describe('displayMessage', function() {
    it('logs to the console the right messages', function(done) {
        // Override console.log to capture output
        const originalLog = console.log;
        let loggedMessage = '';
        console.log = (STDOUT) => {
            loggedMessage = STDOUT;
        };

        // Call the function and check the result
        displayMessage('Hello, World!');
        assert.strictEqual(loggedMessage, 'Hello, World!');

        // Restore the original console.log
        console.log = originalLog;
        done();
    });
});
