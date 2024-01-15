const text = "berry";

switch (text) {
  case "bannana":
    console.log(`J'adore les bannanes`);
    break;
  case "apple":
    console.log("J'aime aussi les pommes");
    break;
  case "avocado":
    console.log("Est-ce un fruit?");
    break;
  default:
    console.log("Je ne connais pas ce fruit");
    break;
}

let userInput = prompt("Choisissez un fruit");
userInput = userInput.toLowerCase(); 


switch (userInput) {
  case "kiwi":
    alert("Les kiwis sont vert et parfois jaunes");
    break;
  case "banane":
    alert("C'est bon les bannanes");
    break;
  case "pomme":
    alert("Pomme verte ou pomme rouge");
    break;
  default:
    alert("Je ne connais pas ce fruit :/");
}
