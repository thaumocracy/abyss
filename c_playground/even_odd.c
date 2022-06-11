#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int input;
    printf("Enter a number: \n");
    scanf("%d", &input);
    if (input % 2 == 0)
    {
        printf("Number %d is even!", input);
    }
    else
    {
        printf("Number %d is odd", input);
    }
    return EXIT_SUCCESS;
}