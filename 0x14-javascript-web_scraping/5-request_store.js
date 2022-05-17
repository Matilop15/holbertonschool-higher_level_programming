#!/usr/bin/node
/*
 * Write a script that gets the contents of a webpage and stores it in a file.
 * The first argument is the URL to request
 * The second argument the file path to store the body response
 */

const axios = require('axios');
const fs = require('fs');
const url = process.argv[2];
const nameFile = process.argv[3];

axios.get(url)
  .then(function (response) {
    fs.writeFile(nameFile, response.data, 'utf-8', function (err, data) {
      if (err) {
        console.error(err);
      }
    });
  });
