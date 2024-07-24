export default function getStudentsIdSum(studentL) {
  if (!Array.isArray(studentL)) {
    return 0;
  }

  return studentL.reduce((sum, student) => sum + student.id, 0);
}
