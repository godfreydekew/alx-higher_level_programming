#!/usr/bin/node
const parsed = process.argv.length > 2 ? parseInt(process.argv[2], 10) : NaN;

if (isNaN(parsed)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parsed; i++) {
    let myx = '';
    for (let k = 0; k < parsed; k++) {
      myx += 'X';
    }
    console.log(myx);
  }
}
