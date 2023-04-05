const year = parseInt(prompt("Enter year"));

function leap() {
  if (year % 4 === 0) {
    document.getElementById('target').innerHTML = year + " is leap year";
  } else {
    document.getElementById('target2').innerHTML = year + " is not leap year";
  }
}

leap();
