export default function updateStudentGradeByCity(studentL, city, newGrades) {
  if (!Array.isArray(studentL) || typeof city !== 'string' || !Array.isArray(newGrades)) {
    return [];
  }

  const studentsLoc = studentL.filter((student) => student.location === city);

  return studentsLoc.map((student) => {
    const nGrade = newGrades.find((grade) => grade === student.id);

    return {
      ...student,
      grade: nGrade ? nGrade.grade : 'N/A'
    };
  });
}