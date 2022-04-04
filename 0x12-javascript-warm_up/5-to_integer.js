#!/usr/bin/node

// script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer

const num = parseInt(process.argv[2]);

if (typeof process.argv[2] === 'undefined') {
  console.log('Not a number');
} else if (!Number.isNaN(num)) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
