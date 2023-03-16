#!/usr/bin/node
/*
  Prints a number of args already printed
  and the new arg value
*/
let count = 0; // Global variable not in the function
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
