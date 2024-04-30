#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    JSON.parse(body).results.forEach(item => {
      item.characters.forEach(chr => {
        if (chr.endsWith('/18/')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
