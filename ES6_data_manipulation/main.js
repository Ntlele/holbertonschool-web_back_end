import getListStudents from "./0-get_list_students";
import getListStudentIds from "./1-get_list_student_ids";
import getStudentsByLocation from "./2-get_students_by_loc";

console.log(getListStudentIds(getListStudents()));
console.log(getStudentsByLocation(getListStudents(), 'San Francisco'));