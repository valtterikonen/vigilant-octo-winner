

  let participants = [];

const number = parseInt(prompt('Insert number of participants'));

for (let i = 0; i < number; i++) {
  const name = prompt('Insert name for participant');
  participants.push(name);
}

participants.sort();

for (let i = 0; i < participants.length; i++) {
  document.getElementById('name').innerHTML += "<li>" + participants[i] + "</li>";
}

