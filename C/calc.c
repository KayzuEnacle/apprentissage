#include <stdio.h>

int main(){
    int add, sub, time, div;
    add = 5 + 5;
    sub = 10 - 5;
    time = 2 * 8;
    div = 10 / 2;
    printf("add : %d, sub : %d, time : %d, div : %d \n", add, sub, time, div);

    double subDiv = 5 / 2;
    printf(" subDiv : %lf \n", subDiv);

    double mod = 4 % 5;
    printf("mod : %lf", mod);
    return 0;
}