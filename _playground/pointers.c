#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    /* code */
    int apples = 12;
    int *ptr = &apples;
    printf("Pointer value is : %p \n", ptr);
    printf("Pointer data is : %d \n", *ptr);
    return EXIT_SUCCESS;
}

// #include <stdio.h>

// int main(void)
// {
//     int a = 10;
//     int b = 2;

//     int *pa = &a;
//     int *pb = &b;

//     printf("Variable a: address=%p \t value=%d \n", pa, *pa);
//     printf("Variable b: address=%p \t value=%d \n", pb, *pb);

//     pa = pb; // теперь указатель pa хранит адрес переменной b
//     printf("Variable b: address=%p \t value=%d \n", pa, *pa);

//     return 0;
// }