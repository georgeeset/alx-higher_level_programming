#!/usr/bin/node
/*
  Converts a number from base 10 to another base
  passed an arg
*/

exports.converter = function (base) {
  return function (number) {
    return parseInt(number, 10).toString(base);
  };
};
