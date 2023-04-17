
const list = []

list.push('First item');
list.push('Second item');
list.push('Third item');

for (i = 0; i < list.length; i++) {
  document.getElementById('target').innerHTML += "<li>" + list[i] + "</li>"
}

