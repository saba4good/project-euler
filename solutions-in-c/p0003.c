/******************************************************************************

                Largest prime factor
Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

*******************************************************************************/

#include <stdio.h>

int main()
{
    long int number=600851475143; // 71*839*1471*6857
    long int N=number;
    long int i, gpf, not_divided;
    
    for(i=2; i<=N; i++)
    {
        not_divided=N%i;
        while(!not_divided)
        {
            gpf=i; // greatest prime factor
            N=N/i; // make N smaller by dividing by a prime factor of 'number'
            not_divided=N%i;
        }
    }
    printf("The greatest prime factor of %d is %d\n", number, gpf);
    
    return 0;
}
