let numbers = [];

while (true) {
  const numb = parseInt(prompt('Insert number'));
  if (numb === 0) {
    break;
  }
  numbers.push(numb);
}

numbers.sort();

console.log(numbers.length);
