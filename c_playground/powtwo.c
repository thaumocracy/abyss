#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int num;
    printf("Input a positive number please: \n");
    while (1)
    {
        scanf("%d", &num);
        if (num == -1)
        {
            printf("Thank you for playing! \n");
            return EXIT_SUCCESS;
        }
        int pow = 2;
        while (pow < num)
        {
            pow = pow * 2;
        }
        printf("Minimum power of 2 is: %d \n", pow);
    }
    return EXIT_SUCCESS;
}