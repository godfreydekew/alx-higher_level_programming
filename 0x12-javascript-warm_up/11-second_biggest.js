#!/usr/bin/node

const x = process.argv.length;

if (x < 4) {
  console.log('0');
} else {
  const myArray = [];
  for (let i = 2; i < x; i++) {
    myArray.push(process.argv[i]);
  }
  myArray.sort(function (a, b) { return b - a; });
  console.log(myArray[1]);
}
