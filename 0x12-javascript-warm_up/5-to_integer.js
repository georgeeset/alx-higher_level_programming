#!/usr/bin/node
const firstArg = process.argv[2];
const number = parseInt(firstArg);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
