export default function updateStudentGradeByCity(studentL, city, newGrades) {
  if (!Array.isArray(studentL) || typeof city !== 'string' || !Array.isArray(newGrades)) {
    return [];
  }

  return studentL
    .filter((student) => student.location === city)
    .map((student) => {
      const nGrade = newGrades.find((grade) => grade.studentId === student.id);

      return {
        ...student,
        grade: nGrade ? nGrade.grade : 'N/A'
      };
    });
}