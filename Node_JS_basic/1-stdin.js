const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log('Welcome to Holberton School, what is your name?');

rl.question('', (INPUT) => {
  console.log(`Your name is: ${INPUT}`);

  rl.close();
  console.log('This important software is now closing');
});
