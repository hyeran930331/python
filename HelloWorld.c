#include <stdio.h>

int main(){
    int i = 0;
    int sum = 0;

    for(i =1; i <=10; i++)
    {
        if (i %3 == 0)
        {
            sum += i;
        }
    }
    printf ("%d",sum)
}
