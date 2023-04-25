#!/usr/bin/node

// printing the status code of a GET request

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  const content = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < content.results.length; i++) {
    const chars = content.results[i].characters;
    for (let k = 0; k < chars.length; k++) {
      if (chars[k].includes('18')) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
