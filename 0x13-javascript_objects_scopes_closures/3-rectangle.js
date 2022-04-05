#!/usr/bin/node

// Write a class Rectangle that defines a rectangle
// f w or h is equal to 0 or not a positive integer, create an empty object
// update task 2: Print a rectangle

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
}

module.exports = Rectangle;
