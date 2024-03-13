#!/usr/bin/node

const array1 = require('./100-data').list;

const map1 = array1.map((x) => x * array1.indexOf(x));
console.log(array1);
console.log(map1);
