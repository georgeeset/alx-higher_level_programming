#!/usr/bin/node

/*
  A script that imports a dictionary of occurences by userid
  and computes a dictionary of user ids by occurrence.
*/

const myDict = require('./101-data').dict;
const newDict = {};

for (const [key, val] of Object.entries(myDict)) {
  if (!(val in newDict)) {
    newDict[val] = [key];
  } else {
    newDict[val].push(key);
  }
}
console.log(newDict);
