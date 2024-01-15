#include <stdio.h>

int main(){
    int var = 3;
    if (var < 3){
        printf("La variable est inférieure à 3\n");
    }else if (var == 3){
       printf("La variable est égale à 3\n");
    }else{
        printf("La variable est supérieure à 3\n");
    }
    return 0;
}