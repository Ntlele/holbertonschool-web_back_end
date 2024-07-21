export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw new Error('Name should be string only.');
    }
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code !== 'string') {
      throw new Error('Code should be string only.');
    }
    this._code = code;
  }

  get [Symbol.toStringTag]() {
    return `${this.code}`;
  }
}
