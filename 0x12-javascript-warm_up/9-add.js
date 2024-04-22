#!/usr/bin/node

/**
 * Adds two integers
 * @param {number} a - The first integer
 * @param {number} b - The second integer
 */
function add(a, b) {
  console.log(parseInt(a) + parseInt(b));
}

if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.length !== 2 || isNaN(parseInt(args[0])) || isNaN(parseInt(args[1]))) {
    console.log('NaN');
  } else {
    add(args[0], args[1]);
  }
}

module.exports = add;

