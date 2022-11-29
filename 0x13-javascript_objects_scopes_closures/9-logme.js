#!/usr/bin/node

let x = -1;
exports.logMe = function (item) {
  function printLog (item) {
    x++;
    console.log(`${x}: ${item}`);
  }
  return printLog(item);
};
