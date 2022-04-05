#!/usr/bin/node

// Write a class Rectangle that defines a rectangle
// f w or h is equal to 0 or not a positive integer, create an empty object
// update task 3: print rectangle and mmultipli values of widht and height

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

module.exports = Rectangle;
