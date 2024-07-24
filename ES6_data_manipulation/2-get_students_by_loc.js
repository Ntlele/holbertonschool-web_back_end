export default function getStudentsByLocation(studentL, city) {
  if (!Array.isArray(studentL) || typeof city !== 'string') {
    return [];
  }

  return studentL.filter((student) => student.location === city);
}
