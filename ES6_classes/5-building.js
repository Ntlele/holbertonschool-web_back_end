export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building
            && typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(sqft) {
    if (typeof sqft !== 'number') {
      throw new Error('sqft is not a number');
    }
    this._sqft = sqft;
  }
}
