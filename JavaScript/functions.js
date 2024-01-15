function greet() {
  let name = prompt("Quel est votre nom?");
  if (name != "") {
    alert(`Bienvenue sur notre site ${name}`);
    console.log(`Bienvenue ${name}`);
  } else {
    alert("Vous devez écrire un nom correcte");
    return greet();
  }
}

// greet();

let maxNb = Math.max(1, 5);
console.log(maxNb);

function max() {
    let nb1 = prompt("Choisissez un nombre");
    let nb2 = prompt("Choisissez un 2eme nombre");


    if(nb1 > nb2) {
        return console.log("Le nombre le plus grand est " + nb1);
    }else{
        return console.log("Le nombre le plus grand est " + nb2);
    }
}

console.log(max());