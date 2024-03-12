#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const x = process.argv.length > 2 ? parseInt(process.argv[2], 10) : NaN;
const y = process.argv.length > 2 ? parseInt(process.argv[3], 10) : NaN;

add(x, y);
