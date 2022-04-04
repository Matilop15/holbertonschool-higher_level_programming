#!/usr/bin/node

//print only the first argument passed if this exists

if (typeof process.argv[2] !== 'undefined') {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
