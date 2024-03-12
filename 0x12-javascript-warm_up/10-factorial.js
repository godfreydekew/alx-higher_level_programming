#!/usr/bin/node

function fact (a) {
  if (a === 1) { return 1; }

  return a * fact(a - 1);
}

const parsed = process.argv.length > 2 ? parseInt(process.argv[2], 10) : NaN;

if (isNaN(parsed)) {
  console.log('1');
} else {
  console.log(fact(parsed));
}
