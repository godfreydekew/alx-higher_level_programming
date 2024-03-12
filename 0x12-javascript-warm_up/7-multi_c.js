#!/usr/bin/node
const parsed = process.argv.length > 2 ? parseInt(process.argv[2], 10) : NaN;

if (isNaN(parsed)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parsed; i++) {
    console.log('C is fun');
  }
}
