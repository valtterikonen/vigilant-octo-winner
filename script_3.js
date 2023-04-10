let dogs = [];

for (let i = 1; i<=6; i++) {
  const name = prompt('Enter name of a dog'+(i-1))
  dogs.push(name)
}

dogs.sort();

for (let i = 0; i < dogs.length; i++) {
  document.getElementById('dogs').innerHTML += "<li>" + dogs + "</li>";
}