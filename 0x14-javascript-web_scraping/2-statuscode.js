#!/usr/bin/node
// a script to print status code on the console

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  console.log('code:', res.statusCode)
});
