let backward = [];

for (let i = 0; i < 5; i++) {
  const number = parseInt(prompt('Insert number ' + (i+1)));
  backward.push(number);
}

for (let i = backward.length - 1; i >= 0; i--) {
  console.log(backward[i]);
}
