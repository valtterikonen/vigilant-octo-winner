const confirmation = prompt("Should I calculate the square root?");

function root() {
  if (confirmation === "yes") {
    const number = parseInt(prompt("Insert number: "));
    if (number < 0) {
      document.getElementById('target').innerHTML = "The square root of a negative number is not defined.";
    } else {
      const sqrt = Math.sqrt(number);
      document.getElementById('target').innerHTML = "The square root of the number is " + sqrt;
    }
  } else if (confirmation === "no") {
    document.getElementById('target').innerHTML = "The square root is not calculated";
  } else {
    return confirmation;
  }
}

root();