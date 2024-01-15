<?php
//$chiffre = null;


// tant que...

while ($chiffre !== 10) {
    $chiffre = (int)readline('Entrez un chiffre : ');
}

echo 'Bravo vous avez trouvé !';


$note = [10, 15, 16];
$eleves = [
    'cm2' => ['Jean', 'Marc', 'Jane', 'Marion'],
    'cm1' => ['Marc', 'Marcelin']
]; 


for ($i = 0; $i < 3; $i ++) {
    echo '- ' . $note[$i] . "\n";
}



foreach ($note as $note) {
    echo "- $note \n";
}

foreach ($eleves as $classe => $eleve) {
    echo "$eleve est dans la classe $classe \n";
}


/*
La classe CM2:
- Jean
- Marc

La clase CM1:
- Emilie...
*/

foreach ($eleves as $classe => $listeleves) {
    echo "La classe $classe: \n";
    foreach ($listeleves as $eleve) {
        echo "- $eleve \n";
    }
    echo "\n";
} 


// ++ = +1


/*
Demande à l'utilisateur de rentrer une note ou de taper le mot "fin"
chaque note est sauvegardée dans un tableau $notes (prenez $notes[])
à la fin on affiche le tableau de note sous forme de liste
*/


// tant que l'utilisateur ne tape pas "fin"

$notes = [];
$action = null;

while ($action !== 'fin') {
    $action = readline('Entrez une nouvelle note (ou \'fin\' pour terminer la saisie) : ');
    // On ajoute la note tapé au tableau notes
    if ($action !== 'fin') {
        $notes[] = (int)$action;
    }
}

// Pour chaque note dans le tableau notes
foreach ($notes as $note) {
    // On affiche "-note"
    echo "- $note \n";
}



/*
on veut demander à l'utilisateur de rentrer les horaires d'ouverture d'un magasin
On demande à l'utilisateur de rentrer une heure et on lui dira si le magasin est ouvert
*/


$horaire = (int)readline('Entrez l\'horaires d\'ouverture du magasin : ');
$heure = (int)readline('Entrez une heure : ');

while ($heure !== $horaire) {
    echo("Le magasion sera fermé \n");
    $heure = (int)readline('Entrez une heure : ');
    if ($heure === $horaire) {
        echo 'Le magasin sera ouvert';
    }
}


// Le juste prix !

$defaultprice = (int)readline('entrez un nombre entre 1 et 10000 : ');
$price = null;

if ($defaultprice <= 10000) {
    $price = (int)readline('Entrez un nombre : ');
    while ($price !== $defaultprice) {
        if ($price < $defaultprice) {
            echo "C'est plus \n";
            $price = (int)readline('Entrez un nombre : ');
        }elseif ($price > $defaultprice) {
            echo "C'est moins \n";
            $price = (int)readline('Entrez un nombre : ');
        }else {
            echo 'Bravo vous avez trouvé le nombre !';
        }
    }
}elseif ($defaultprice > 10000) {
    echo 'La valeur est trop grande !';
}
?>