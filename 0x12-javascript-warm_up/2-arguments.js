#!/usr/bin/node

// If no arguments are passed to the script, print “No argument”
// If only one argument is passed to the script, print “Argument found”

const len = process.argv.length;
if (len === 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
