#include <stdio.h>

int main(int argc, char *argv[]){

    int age = 17;

    switch (age){
    case 2:
    printf("Salut bebe !");
    break;
    case 6:
    printf("Salut gamin !");
    break;
    case 12:
    printf("Salut jeune !");
    break;
    case 16:
    printf("Salut ado !");
    break;
    case 18:
    printf("Salut adulte !");
    break;
    case 68:
    printf("Salut papy !");
    break;
    default:
    printf("Je n'ai aucune reponse pour ton age");
    break;
    }
}