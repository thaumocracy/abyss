#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b);
int main(void)
{
    int a = 1;
    int b = 2;
    int *pa = &a;
    int *pb = &b;
    /* code */
    printf("Before first swap: A:%d B:%d \n", a, b);
    swap(pa, pb);
    printf("After first swap: A:%d B:%d \n", a, b);
    swap(pb, pa);
    printf("after second swap: A:%d B:%d \n", a, b);
    swap(pa, pb);
    return EXIT_SUCCESS;
}

void swap(int *a, int *b)
{
    int temp = *a;
    *b = *a;
    *a = temp;
}