#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const myDictionary = {};
let count = 0;
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const myResponse = JSON.parse(body);
    myResponse.forEach(usr => {
      if (myDictionary[usr.userId] === undefined) {
        myResponse.forEach(tasks => {
          if (tasks.completed && tasks.userId === usr.userId) {
            count += 1;
          }
        });
        myDictionary[usr.userId] = count;
        count = 0;
      }
    });
    console.log(myDictionary);
  }
});
