#!/usr/bin/node
/*
 *Write a script that computes the number of tasks completed by user id.
 *The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 *Only print users with completed task
 */

const axios = require('axios');
const url = process.argv[2];
let cantidad = 0;
const dict = {};

axios.get(url)
  .then(function (response) {
    for (const num in response.data) {
      const userid = response.data[num].userId;
      const task = response.data[num].completed;
      if (num !== 0) {
	if (dict[userid] >= 1) {
          cantidad = dict[userid];
        } else {
          cantidad = 0;
        }
      }
      if (userid && task) {
        cantidad += 1;
      }
      dict[userid] = cantidad;
    }
    console.log(dict);
  })
  .catch(function (err) {
    console.error(err);
  });
