class Node {
  constructor(value){
    this.value = value,
    this.next = null
  }
}

class Stack {
  constructor(){
    this.array = []
  }

  peek(){
    return this.array[this.array.length - 1]
  }

  push(value){
    this.array.push(value)
    return this
  }
  pop(){
    this.array.pop()
    return this
  }
}

const myStack = new Stack()

console.log(myStack.peek())
console.log(myStack.push('google'))
console.log(myStack.push('udemy'))
console.log(myStack.pop())

