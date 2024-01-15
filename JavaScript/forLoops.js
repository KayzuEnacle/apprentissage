for (let i = 0; i <= -1; i++) {
  console.log(i);
  if (i === 20) {
    console.log("Tu as atteint le nombre 20");
    continue; // Skip le nombre 20
  }
}

const texts = ["Bonjour", "Salut", "Yo"];

for (let n = 0; n < texts.length; n++) {
  // console.log(texts[n]);
}

// FOR OF

for (let text of texts) {
  console.log(text.indexOf(text));
}



// FOREACH (ne fonctionne uniquement avec des tableaux)

texts.forEach(function(type){
  console.log(type)
})