// const helloWorld: string = "Hello World"


// function sayHello(input: string): string {
//     const newString = input.split('')
//     return newString.reverse().join('')
// }


// console.log(sayHello(helloWorld))


// function mul(num: number = 2): number {
//     return num ** 2;
// }




function test(person: { first: string, last: string, age: number }): { first: string, last: string, age: number } {
    return {
        first: person.first + '5',
        last: person.last + '5',
        age: person.age + 3,
    }
}

test({
    first: 'test',
    last: 'test',
    age: 32,
})