#!/usr/bin/node

const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/people/18/';

axios.get(url)
  .then(function (response) {
    const rute = response.data.films;
    const leng = rute.length;
    console.log(leng);
  });
  .catch (function (err) {
    console.log(err);
  });
