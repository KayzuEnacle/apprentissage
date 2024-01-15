const usersList = [
    1,
    "LeLaitier",
    "Jhon",
    "User",
    true
];


console.log(usersList[0]);

usersList.pop(); // Retire le dernier element
usersList.push("NEW"); // Ajoute un element
usersList.shift(); // Retire le premier element
usersList.unshift("NEW"); // Ajoute un element au début 



console.log(usersList);
console.log(usersList.length)
console.log(usersList.indexOf("Kayzu"))