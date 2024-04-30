#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const myResponse = JSON.parse(body);

    myResponse.characters.forEach(char => {
      request(char, (error, res, mybody) => {
        if (error) {
          console.log(err);
        } else {
          const myChar = JSON.parse(mybody);
          console.log(myChar.name);
        }
      });
    });
  }
});
