const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const lines = data.trim().split('\n');
    const studentCount = {};
    const studentNames = {};

    lines.forEach(line => {
      const [firstName, field] = line.split(',');
      if (firstName && field) { // Ensure that both values are present
        if (!studentCount[field]) {
          studentCount[field] = 0;
          studentNames[field] = [];
          }
          studentCount[field]++;
          studentNames[field].push(firstName);
      }
    });

    console.log(`Number of students: ${lines.length}`);
    for (const field in studentCount) {
      console.log(`Number of students in ${field}: ${studentCount[field]}. List: ${studentNames[field].join(', ')}`);
    }

  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
