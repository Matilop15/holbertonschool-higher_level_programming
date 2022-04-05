#!/usr/bin/node

// Write a class Rectangle that defines a rectangle
// f w or h is equal to 0 or not a positive integer, create an empty object

class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || h <= 0) || !w || !h) {
      return NaN;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
