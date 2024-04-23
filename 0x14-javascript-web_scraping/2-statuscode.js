#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
    console.log(response.statusCode || err);
});
