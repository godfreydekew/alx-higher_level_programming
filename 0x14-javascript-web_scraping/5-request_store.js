#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (error) {
      if (error) throw error;
    });
  }
});
