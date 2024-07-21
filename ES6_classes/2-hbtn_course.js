function ValidInputs(name, length, students) {
  if (typeof name !== 'string') {
    throw new TypeError('name must be a string');
  }
  if (typeof length !== 'number') {
    throw new Error('length must be a number');
  }
  if (!Array.isArray(students)) {
    throw new Error('students must be the an Array');
  }
}

export default class HolbertonCourse {
  constructor(name = '', length = 0, students = []) {
    ValidInputs(name, length, students);
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }
    this._name = name;
  }

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw new TypeError('length must be a number');
    }
    this._length = length;
  }

  get students() {
    return this._students;
  }

  set students(students) {
    if (!Array.isArray(students)) {
      throw new Error('students must be an array');
    }
    this._students = students;
  }
}
