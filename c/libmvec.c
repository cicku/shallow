/*  TL;DR: vmovsd replaces fstpl

    On the basis of libmvec mathlib introduced in glibc 2.22 onwards,
    there is support for new CPU instructions like SSE4.2/AVX2
    you can generate the assembler code via (required GCC 4.8+):

    $ gcc -S ./libmvec.c -fopenmp -ffast-math -mavx2 -lm
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*  -fno-aggressive-loop-optimizations if you want to use ##define instead
of const int.
#define N 100
*/

int main (void) {
    const int N = 100;
    double a[N];
    double b[N];

    for (int i = 1; i < (N+1); i++) {
        b[i] = cos(a[i]);
        printf("cos(%d) is: %f\n", i, b[i]);
    }
    exit(EXIT_SUCCESS);
}
