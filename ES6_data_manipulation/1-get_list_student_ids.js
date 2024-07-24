export default function getListStudentIds(arrayL) {
  if (!Array.isArray(arrayL)) {
    return [];
  }

  return arrayL.map((student) => student.id);
}
