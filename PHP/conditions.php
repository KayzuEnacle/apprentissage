<?php

// variable de l'action
// $act = (int)readline('Entrez votre action (1 : attaquer / 2 : défendre / 3 : passer son tour ');

// switch (comme le if else...)

switch ($act) {
    case 1:
        echo 'J\'attaque !';
        break;
    case 2:
        echo 'Je défend !';
        break;
    case 3:
        echo 'Je passe mon tour !';
        break;
    default:
        echo 'Comande invalide !';
}


// ou alors if else...
if ($act === 1) {
    echo 'J\'attaque !';
}elseif ($act === 2) {
    echo 'Je défend !';
}elseif ($act === 3) {
    echo 'Je passe mon tour !';
}else {
    echo 'Comande invalide !';
} 

// Faire plusieurs conditions
$heure = (int)readline('Entrez une heure : ');

if ((9 > $heure && $heure > 12) || (14 > $heure && $heure > 17)) {
    echo 'Le magasin sera fermé';
}else {
    echo 'Le magasin sera ouvert';
}

// vrais && vrais = vrais
// vrais && faux = faux
// faux && faux = faux

// vrais || vrais = vrais
// vrais || faux = vrais
// faux || faux = faux

// && = et
// || = ou
// ! = le contraire de...

?>