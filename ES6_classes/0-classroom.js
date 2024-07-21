export default class ClassRoom {
  constructor(maxStudentsSize = 0) {
    if (typeof maxStudentsSize !== 'number') {
      throw new Error('Max student size should be a number');
    }
    this._maxStudentsSize = maxStudentsSize;
  }
}
