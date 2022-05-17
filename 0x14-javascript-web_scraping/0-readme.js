#!/usr/bin/node
/*
# Write a script that reads and prints the content of a file.
The first argument is the file path
*/

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
