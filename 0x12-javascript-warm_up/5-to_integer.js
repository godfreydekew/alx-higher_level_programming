#!/usr/bin/node
const parsed = process.argv.length > 2 ? parseInt(process.argv[2], 10) : NaN;

if (isNaN(parsed)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsed}`);
}
