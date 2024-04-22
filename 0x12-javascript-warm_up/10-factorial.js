#!/usr/bin/node

/**
 * Computes the factorial of a given number recursively.
 * @param {number} n - The number to compute factorial for.
 * @returns {number} - The factorial of n.
 */
function factorial (n) {
  if (isNaN(n)) return 1;
  if (n === 0 || n === 1) return 1;
  return n * factorial(n - 1);
}

const args = process.argv.slice(2);
const num = parseInt(args[0]);

console.log(factorial(num));

