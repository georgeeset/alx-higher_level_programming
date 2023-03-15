#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let argList = process.argv.slice(2);
  argList = argList.sort(
    function (a, b) {
      return (a - b);
    }
  );
  console.log(argList[1]);
}
