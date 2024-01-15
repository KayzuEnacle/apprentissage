<?php
// $nom = "Doe";

// function hello ($prenom = null){
//     global $nom;
//     if($prenom === null){
//         return 'Bonjour';
//     }
//     return 'Hello ' . $prenom . " " . $nom . "\n";
// }

// echo hello() . "\n";
// echo hello('Mike');


function ouinon($phrase){
    while (true){
        $reponse = readline($phrase . "(o) oui / (n) non");
        if($reponse ==="o"){
            return true;
        }elseif($reponse === 'n'){
            return false;
        }
    }    
}

$resultat = ouinon('Oui ou non?');
var_dump($resultat);