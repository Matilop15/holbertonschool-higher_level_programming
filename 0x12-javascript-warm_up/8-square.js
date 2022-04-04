#!/usr/bin/node

// script that prints a square

const num = parseInt(process.argv[2]);

if (Number.isNaN(num)) {
	  console.log('Missing size');
} else {
  let i = 0;
  while (i < num) {
  console.log('X'.repeat(num));
  i++;
 }
}
