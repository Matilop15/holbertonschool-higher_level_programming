#!/usr/bin/node

// Write a function that increments and calls a function.

function addMeMaybe (nb, theFunction) {
  theFunction(nb + 1);
}
module.exports.addMeMaybe = addMeMaybe;
