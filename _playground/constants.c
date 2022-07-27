#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    const int moon_landing = 1969;
    const double speed_of_light = 299792458.;
    const double pi = 3.142;
    const unsigned hexaDead = 0xDEADU;
    const unsigned hexaSecret = 51966U;
    printf("----------------- \n");
    printf("Moon Landing: \n %10d \n %010d \n\n", moon_landing, moon_landing);
    printf("----------------- \n");
    printf("Speed of Light: \n %.0f \n %.3e \n \n", speed_of_light, speed_of_light);
    printf("----------------- \n");
    printf("PI:  %.2f \n %+.1e \n \n", pi, pi);
    printf("----------------- \n");
    printf("Hexa dead: \n  0x%X \n %6u \n\n", hexaDead, hexaDead);
    printf("----------------- \n");
    printf("Hexa Secret: \n %x \n \n");
    printf("----------------- \n");
    return EXIT_SUCCESS;
}