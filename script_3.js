  let sum = 0;
  let product = 1;
  let numbers = [];

  for (let i = 0; i < 3; i++) {
    const number = parseInt(prompt('Insert number'));
    numbers.push(number);
    sum += number;
    product *= number;
  }

  const avg = sum / numbers.length;

  document.getElementById('target').innerHTML ="<p>Sum: " + sum + "</p>";
  document.getElementById('target2').innerHTML ="<p>Product: " + product + "</p>";
  document.getElementById('target3').innerHTML ="<p>Average: " + avg + "</p>";

  