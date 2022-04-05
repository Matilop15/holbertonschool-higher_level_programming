#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || h <= 0) || !w || !h) {
      return NaN;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let count = 0; count < this.width; count++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  double () {
    const newWidth = this.width * 2;
    const newHeight = this.height * 2;
    this.width = newWidth;
    this.height = newHeight;
  }

  rotate () {
    const rotWidth = this.height;
    const rotHeight = this.width;
    this.width = rotWidth;
    this.height = rotHeight;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let row = '';
    for (let count = 0; count < this.width; count++) {
      if (c === 'undefined') {
        row += 'X';
      } else {
        row += 'C';
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
