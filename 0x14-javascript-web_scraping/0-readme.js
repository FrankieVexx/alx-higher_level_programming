#!/usr/bin/node
// This is a script that reads a text file

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, content) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(content);
});
