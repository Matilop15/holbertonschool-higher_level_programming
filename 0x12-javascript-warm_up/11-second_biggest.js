#!/usr/bin/node

// script that searches the second biggest integer in the list of arguments.

const arrayValues = process.argv;
const newArray = [];
for (let i = 2; i < arrayValues.length; i++) {
  newArray[i - 2] = parseInt(arrayValues[i]);
}
if (arrayValues.length < 4) {
  console.log(0);
} else {
  newArray.sort();
  newArray.reverse();
  console.log(newArray[1]);
}
