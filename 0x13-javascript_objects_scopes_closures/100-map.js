#!/usr/bin/node
// Imports an array and computes a new array

const list = require('./100-data').list;
console.log(list);
const array = list.map((x, idx) => x * idx);
console.log(array);
