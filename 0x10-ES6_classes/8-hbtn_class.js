export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  [Symbol.toPrimitive](cast) {
    if (cast === 'number') return this._size;
    if (cast === 'string') return this._location;
    return null;
  }
}
