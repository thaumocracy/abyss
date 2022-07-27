console.log("Hello world");

function runningSum(nums) {
  let output = [];
  for (let i = 0; i < nums.length; i++) {
    let sum = 0;
    for (let j = 0; j <= i; j++) {
      sum += nums[j];
    }
    output.push(sum);
  }
  return output;
}

console.log(runningSum([1, 2, 3, 4]));
console.log(runningSum([1, 1, 1, 1, 1]));
console.log(runningSum([3, 1, 2, 10, 1]));
