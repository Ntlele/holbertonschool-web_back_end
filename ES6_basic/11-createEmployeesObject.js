export default function createEmployeesObject(departmentName, employees) {
  const employees2 = [];

  for (const idx of employees) {
    employees2.push(idx);
  }
  return { [departmentName]: employees2 };
}
