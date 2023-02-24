#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    printf("\n ===== IGNITION ===== \n");
    typedef enum
    {
        none = 0,
        low = 5,
        medium = 10,
        high = 12,
        maximum = 20,
    } Modes;
    printf("Mode is none. Power is: %d", none);
    printf("Mode is low. Power is: %d", low);
    printf("Mode is medium. Power is: %d", medium);
    printf("Mode is high. Power is: %d", high);
    printf("Mode is maximum. Power is: %d", maximum);
    printf("Mode is none. Power is: %d", none);
    return EXIT_SUCCESS;
}