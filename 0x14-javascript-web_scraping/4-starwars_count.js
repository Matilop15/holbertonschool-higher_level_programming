#!/usr/bin/node
/*
* Write a script that prints the number of movies where the character “Wedge Antilles” is present.
* The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
* Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
*/

const axios = require('axios');
const url = process.argv[2];
let count = 0;

axios.get(url)
  .then(function (response) {
    const resp = response.data.results;
    for (let i = 0; i < 7; i++) {
      if (resp[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  })
  .catch(function (err) {
    console.log(err);
  });
