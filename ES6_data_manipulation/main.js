import getListStudents from "./0-get_list_students";
import getListStudentIds from "./1-get_list_student_ids";
import getStudentsByLocation from "./2-get_students_by_loc";
import getStudentsIdSum from "./3-get_ids_sum";
import createInt8TypedArray from "./5-typed_arrays";

console.log(getListStudentIds(getListStudents()));
console.log(getStudentsByLocation(getListStudents(), 'San Francisco'));
console.log(getStudentsIdSum(getListStudents()));
console.log("\n");
console.log(createInt8TypedArray(10, 2, 89));