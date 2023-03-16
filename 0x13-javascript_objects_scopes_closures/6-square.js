#!/usr/bin/node
/*
  A class sq that defines a sq and inherits
  from Square of 5-square.js
*/
const squareOne = require('./5-square');
module.exports = class Square extends squareOne {
/* instance method that prints the rectangle using 'C' */
 charPrint (C) {
	if (C == undefined) {
	  super.print();
	} else {
	    for (let x = 0; x < this.width; x++) {
	     console.log(C.repeat(this.width));
	    }
	}
    }
}
