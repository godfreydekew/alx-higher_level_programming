#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let myx = '';
      for (let k = 0; k < this.width; k++) {
        myx += 'X';
      }
      console.log(myx);
    }
  }

  rotate () {
    this.height = this.height + this.width;
    this.width = this.height - this.width;
    this.height = this.height - this.width;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
