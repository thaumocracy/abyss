var helloWorld = "Hello World";
function sayHello(input) {
  var newString = input.split("");
  return newString.reverse().join("");
}
console.log(sayHello(helloWorld));
function mul(num) {
  if (num === void 0) {
    num = 2;
  }
  return Math.pow(num, 2);
}
