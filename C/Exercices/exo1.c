#include <stdio.h>

// Faire une fonction de somme
int main(){
    printf("Entrez un premier nombre : ");
    int value1 = 0;
    scanf("%d", &value1);
    printf("Entrez un second nombre : ");
    int value2 = 0;
    scanf("%d", &value2);

    int sum = value1 + value2;
    printf("%d + %d = %d", value1, value2, sum);
}