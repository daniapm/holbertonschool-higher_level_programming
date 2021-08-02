#!/usr/bin/node
const myObject = {
	type: 'object',
	value: 12
  };
  console.log(myObject);
function incr (){
	myObject.incr = myObject.value += 1
	return myObject.incr
};
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
