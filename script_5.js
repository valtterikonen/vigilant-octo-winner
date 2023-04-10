let numbers = [];
let prevNumb = null;

while (true) {
  const numb = parseInt(prompt('Insert number'));
  if (numb === prevNumb) {
    break;
  }
  numbers.push(numb);
  prevNumb = numb;
}

numbers.sort();

console.log(numbers.length);
