#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    float num;
    scanf("%f", &num);
    printf("Number is: %f \n", num);
    double test = num - (int)num;
    printf("Number is: %f \n", test);
    return EXIT_SUCCESS;
}