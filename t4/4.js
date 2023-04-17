'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const selectElement = document.getElementById("target");

for (let i = 0; i < students.length; i++) {
  const option = document.createElement("option");
  option.value = students[i].value;
  option.text = students[i].name;
  selectElement.appendChild(option);
}