#!/usr/bin/node

const Rectangle = require('./1-rectangle');

//  class Rectangle that defines a rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size);
    this.height = size;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Square;
