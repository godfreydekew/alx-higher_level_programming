#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    const ch = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myx = '';
      for (let k = 0; k < this.width; k++) {
        myx += ch;
      }
      console.log(myx);
    }
  }
};
