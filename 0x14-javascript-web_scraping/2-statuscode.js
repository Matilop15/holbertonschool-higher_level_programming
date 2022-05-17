#!/usr/bin/node
/*
Write a script that display the status code of a GET request.

The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
You must use the module axios
*/

const axios = require('axios');
const url = process.argv[2];

axios.get(url)
  .then(function (response) {
    console.log('code: ' + response.status);
  })
  .catch(function (err) {
    console.log('code: ' + err.response.status);
  });
