#!/usr/bin/node

// script that prints x times “C is fun”

const num = parseInt(process.argv[2]);

if (Number.isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
