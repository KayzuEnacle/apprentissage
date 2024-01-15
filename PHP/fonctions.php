<?php

$variable = demo($variable, '1234');
$echo = demo($variable, '1234'); 



$variable = readline();
var_dump($variable, 123, 5, 57, 9, "Ahoy !");



// Test de fonction

    // Voir si un mot est un palyndrome 
    // = palyndrome (mot se lisant dans les deux sans (kayak))


$mot = readline('Veuillez entrez un mot : ');

$minmot = strtolower($mot);
$envmot = strrev($minmot);

if($envmot === $minmot) {
    echo("$mot peut se lire à l'envers ($minmot)");
}else {
    echo("$mot Ne peut pas se lire à l'envers ($minmot)");
}


    // faire la moyenne de notes dans un tableau


$notes = [10, 20, 13];

$sum = array_sum($notes);
$result = $sum / count($notes);
echo("Vous avez " . round($result) . " de moyenne");



$notes = [10, 20, 13];
$notesrev = array_reverse($notes); // Sert à inverser le tableau
$ordernotes = sort($notes); // Sert à mettre par ordre croissance le tableau
print_r($notes);
print_r($notesrev);
print_r($ordernotes);


$notes = [10, 20, 13];
$notes2 = &$notes; // & = Fonction mutable (Elle modifie les comportement des variables qui lui sont passés)
$notes2[] = 10;
var_dump($notes, $notes2);


while(true) {
    $mot = readline('Entrez votre mot : ');
    if($mot === '') {
        exit('Fin du programme'); // Sert à s'arrêter et ne plus continuer
    }
    $reverse = strtolower(strrev($mot));
    if(strtolower($mot) === $reverse) {
        echo "Ce mot est un palyndrome \n";
    }else {
        echo "Ce mot n'est pas un palyndrome \n";
    }
}


    // Censure d'insultes (2 manières)


$insultes = ['merde', 'putain', 'con', 'enculer', 'ta gueule'];
$phrase = readline('Entrez une phrase : ');
foreach($insultes as $insulte) {
    $replace = str_repeat('*', strlen($insulte));
    $phrase = str_replace($insulte, $replace, $phrase);
}
echo $phrase;


    // Ou

$insultes = ['merde', 'putain', 'con', 'enculer', 'ta gueule'];
$asterisque = [];
foreach($insultes as $insulte) {
    $asterisque[] = str_repeat('*', strlen($insulte));
}
$phrase = readline('Entrez une phrase : ');
$phrase = str_replace($insultes, $asterisque, $phrase);
echo $phrase;




    // Exercice : Ne pas censurer la première lettre du mot

$insultes = ['merde', 'putain', 'con', 'enculer', 'ta gueule'];
$asterisque = [];
foreach($insultes as $insulte) {
    // Trouver la première lettre du mot (substr)
    // Trouver la taille du mot (-1)
    // Concatener la première lettre avec le str_repeat
    $asterisque[] = substr($insulte, 0, 1) . str_repeat('*', strlen($insulte) - 1);
}
$phrase = readline('Entrez une phrase : ');
$phrase = str_replace($insultes, $asterisque, $phrase);
echo $phrase;
?>