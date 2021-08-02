#!/usr/bin/node
//  function that returns the addition of 2 integers.
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
