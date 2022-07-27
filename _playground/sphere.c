#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    float radius;
    scanf("%f", &radius);
    printf("Radius is: %3f \n\n", radius);
    float surface = 3.14 * 4 * radius * radius;
    printf("Surface is: %3.2f \n\n", surface);
    float volume = (((radius * radius * radius) * 3.14) / 3) * 4;
    printf("Volume is: %3.2f", volume);
    return EXIT_SUCCESS;
}