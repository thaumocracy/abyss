#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    typedef enum
    {
        Mercury = 88,
        Venus = 225,
        Earth = 365,
        Mars = 687,
        Jupiter = 4333,
        Saturn = 10759,
        Uranus = 30687,
        Neptune = 60190,
    } Planets;
    int mul;
    for (int i = 1; i < 10000; i++)
    {
        mul = Earth * i;
        if (mul % Mercury == 0 && mul % Venus == 0 && mul % Earth == 0)
        {
            break;
        }
    }
    printf("----------------------------------- \n");
    printf("Stuff happens once in %d  days\n", mul);
    printf("Mercury does %d orbits \n", mul / Mercury);
    printf("Venus   does %d orbits \n", mul / Venus);
    printf("Earth   does %d orbits \n", mul / Earth);
    printf("----------------------------------- \n");
    return EXIT_SUCCESS;
}