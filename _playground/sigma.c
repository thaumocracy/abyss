#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    printf("BIG SIGMA SIGN: \n");
    printf("------------------------------\n");
    int base = 10;
    int peak = 5;
    int height = 12;
    for (int i = 0; i <= base; i++)
    {
        printf("#");
    }
    printf("\n");
    for (int i = 1; i < peak; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf(" ");
        }
        printf("#\n");
    }
    printf("     #\n");
    for (int i = peak - 1; i > 0; i--)
    {
        for (int j = i; j > 0; j--)
        {
            printf(" ");
        }
        printf("#\n");
    }
    for (int i = 0; i <= base; i++)
    {
        printf("#");
    }
    printf("\n");
    printf("------------------------------\n");
    printf("Base width: %d \n", base);
    printf("Peak width: %d \n", peak);
    printf("Total height: %d \n", height);
    printf("------------------------------\n");
}