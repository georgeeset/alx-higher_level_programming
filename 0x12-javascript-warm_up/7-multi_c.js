#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (!isNaN(num)) {
  for (let n = 0; n < num; n++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
