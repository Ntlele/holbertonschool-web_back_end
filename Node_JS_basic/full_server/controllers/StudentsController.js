import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(request, response, db) {
    readDatabase(db)
      .then((studentsByField) => {
        response.write('This is the list of our students');
        let strStudents = '';
        for (const field in studentsByField) {
          let strList = '';
          for (const student of studentsByField[field]) {
            if (strList.length > 0) {
              strList += ', ';
            }
            strList += student;
          }
          strStudents += `Number of students in ${field}: ${studentsByField[field].length}. List: ${strList}\n`;
        }
        response.write(strStudents.slice(0, -1));
        response.send(200);
      })
      .catch(() => {
        response.send(500, 'Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response, db) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.send(500, 'Major parameter must be CS or SWE');
    } else {
      readDatabase(db)
        .then((fields) => {
          const students = fields[major];
          response.send(200, `List: ${students.join(', ')}`);
        })
        .catch(() => response.send(500, 'Cannot load the database'));
    }
  }
}
