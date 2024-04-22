#!/usr/bin/node

/**
 * callMeMoby - Executes a given function a specified number of times.
 * @param {number} x - The number of times to execute the function.
 * @param {function} theFunction - The function to be executed.
 */
function callMeMoby(x, theFunction) {
  if (x > 0) {
    theFunction();
    callMeMoby(x - 1, theFunction);
  }
}

module.exports = { callMeMoby };

