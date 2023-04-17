
const mylist = document.createElement('ul');


const firstItem = document.createElement('li');
firstItem.textContent = 'First item';
mylist.appendChild(firstItem);

const secondItem = document.createElement('li');
secondItem.textContent = 'Second item';
mylist.appendChild(secondItem);

const thirdItem = document.createElement('li');
thirdItem.textContent = 'Third item';
mylist.appendChild(thirdItem);


document.getElementById('target').appendChild(mylist);