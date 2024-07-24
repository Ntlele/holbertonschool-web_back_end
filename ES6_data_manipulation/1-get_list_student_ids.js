export default function getListStudentIds(array_L) {
  if (!Array.isArray(array_L)) {
    return [];
  }

  return array_L.map(student => student.id);
}