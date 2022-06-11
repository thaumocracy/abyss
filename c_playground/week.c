#include <stdio.h>
#include <stdlib.h>

int main(void)
{

    typedef enum
    {
        Monday = 1,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday,
        Sunday,
    } Week;

    Week day;
    scanf("%u", &day);
    switch (day)
    {
    case Monday:
        printf("Monday!");
        break;
    case Tuesday:
        printf("Tuesday!");
        break;
    case Wednesday:
        printf("Wednesday!");
        break;
    case Thursday:
        printf("Thursday!");
        break;
    case Friday:
        printf("Thursday!");
        break;
    case Saturday:
        printf("Saturday!");
        break;
    case Sunday:
        printf("Sunday!");
        break;
    default:
        printf("What?");
    }
}