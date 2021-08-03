#!/usr/bin/node
// function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  const result = list.filter(element => element === searchElement).length;
  return result;
};
