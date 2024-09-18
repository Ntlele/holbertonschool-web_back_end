const fs = require('fs');

async function readDatabase(path) {
  return new Promise((resolve, reject) => {
    try {
      const data = fs.readFile(path, 'utf8');
      const linesArray = data.split('\n');
      const studentsByField = {};
      linesArray.shift();
      for (const line of linesArray) {
        const splittedLine = line.split(',');
        if (splittedLine.length === 4) {
          if (splittedLine[3] in studentsByField) {
            studentsByField[splittedLine[3]].push(splittedLine[0]);
          } else {
            studentsByField[splittedLine[3]] = [splittedLine[0]];
          }
        }
      }
      resolve(studentsByField);
    } catch (err) {
      reject(new Error('Cannot load the database'));
    }
  });
}

module.exports = readDatabase;
