#include <stdio.h>

void main()
{
    int x, m, n = 0;
    printf("input x : ");
    scanf("%d", &x);
    m = x;
    do
    {
        n++;
        x /= 10;
    } while (x > 0);
    printf("%d is %d bit number .");
}
}