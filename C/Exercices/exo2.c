#include <stdio.h>

int main(){
    printf("== Menu == \n 1. Royal Cheese \n 2. Mc Deluxe \n 3. Mc Bacon \n 4. Big Mac \n Votre choix ?  : ");
    int choice = 0;
    scanf("%d", &choice);

     switch (choice){
        case 1:
     printf("Tu as choisis le menu Royal Cheese");
        break;
        case 2:
     printf("Tu as choisis le menu Mc Deluxe");
        break;
        case 3:
     printf("Tu as choisis le menu Mc Bacon");
        break;
        case 4:
     printf("Tu as choisis le menu Big Mac");
        break;
        default:
        printf("Je ne connais pas ce menu...");
        break;
     }
}