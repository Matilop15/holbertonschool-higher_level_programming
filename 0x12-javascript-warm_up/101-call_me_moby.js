#!/usr/bin/node

// Write a function that executes x times a function.

function callMeMoby (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
}
module.exports.callMeMoby = callMeMoby;
