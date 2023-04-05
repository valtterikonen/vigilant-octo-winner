function random() {
  const tribes = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"];
  const randomIndex = Math.floor(Math.random() * tribes.length);
  return tribes[randomIndex];
}

const name = prompt('Type your name');
document.getElementById('target').innerHTML = name + ", you are " + random();
