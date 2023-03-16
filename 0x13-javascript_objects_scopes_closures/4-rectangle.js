#!/usr/bin/node
/* A class Rectangle that definies a rectangle */

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const ram = this.width;
    this.width = this.height;
    this.height = ram;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
