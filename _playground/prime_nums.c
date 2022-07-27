#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPrime(int num);
int main()
{
    printf("\n=== Prime Numbers ===\n\n");

    const int MAX = 1000;

    int upperLimit;
    printf("Enter the upper limit: ");
    scanf("%d", &upperLimit);
    if (upperLimit < 2 || upperLimit > MAX)
    {
        printf("Error: must be 2 < limit < MAX\n");
        /* cleanup and exit */
        goto exit_program;
    }

    printf("Prime numbers up to %d:\n", upperLimit);

    for (int number = 2; number < upperLimit; number++)
    {
        if (isPrime(number))
        {
            printf("%d\n", number);
        }
    }

    int lowerLimit;
    printf("Enter the lower limit: ");
    scanf("%d", &lowerLimit);
    if (lowerLimit < 2 || lowerLimit > MAX)
    {
        printf("Error: must be 2 < limit < MAX\n");
        goto exit_program;
    }

    int firstPrimeNumber = -1;

    for (int number = lowerLimit; number < MAX; number++)
    {

        if (isPrime(number))
        {
            firstPrimeNumber = number;
            break;
        }
    }

    if (firstPrimeNumber == -1)
    {
        printf("Cannot find prime numbers above %d\n", lowerLimit);
    }
    else
    {
        printf("The first prime number above %d is %d\n", lowerLimit, firstPrimeNumber);
    }

exit_program:
    printf("\n----------------------\n");
    printf("Some dummy cleanup code...");
    return EXIT_SUCCESS;
}

bool isPrime(int num)
{
    bool isPrime = true;
    for (int i = 2; i < num; i++)
    {
        if (num % i == 0)
        {
            isPrime = false;
            break;
        }
    }

    return isPrime;
}