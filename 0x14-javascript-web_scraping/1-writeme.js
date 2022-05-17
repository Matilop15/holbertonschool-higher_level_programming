#!/usr/bin/node
/*
Write a script that writes a string to a file.
The first argument is the file path
The second argument is the string to write
*/

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
