// Egal à

//  5 == 5 = true
//  4 == 5 = false

// Est différent de

//  4 != 3 = true
//  4 != 4 = false

// TOUJOURS UTILISER LE TRIPLE EQUALS (===)

// Conditions

const access = true;

if (access) {
  console.log("TRUE");
} else {
  console.log("FALSE");
}

const old = 24;
const bank = 50;

if (old >= 18 && bank >= 15) {
  console.log("Vous avez accès");
} else {
  console.log("Vous n'avez pas accès");
}

// && = et
// || = ou

// Truthy et Falsey

const age = null;

if (age) {
  console.log("C'est une valeur est Vraie");
} else {
  console.log("C'est une valeur Fausse");
}

// La valeur est fausse si : False, 0, "", null, undefined, NaN