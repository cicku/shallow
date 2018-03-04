#include "stdio.h"

void swapval(int *x, int *y) {
    int tmp;
    tmp = *x; *x = *y; *y = tmp;
}

void main(void) {
    printf("test\n");
    int a = 10; int b = 20;
    printf("Before swap, a is %d, b is %d.\n", a, b);
    swapval(&a, &b);
    printf("After swap, a is %d, b is %d.\n", a, b);
}
