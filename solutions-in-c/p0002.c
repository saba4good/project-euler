/******************************************************************************
                            Fibonacci sequence
Problem:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
*******************************************************************************/

#include <stdio.h>

int main()
{
    int a=1, b=2; // start numbers are initialized here
    int c=a+b, sum=3;
    int limit = 4000000; // the largest number to which the sequence can grow
    int s_even; // the sum of the even numbers in the sequence
    int is_b_odd, is_a_odd;
    
    while (c<=limit)
    {
        sum+=c;
        a=b;
        b=c;
        c=a+b;
    }
    
    is_b_odd = b%2;
    if (is_b_odd)
    {
        sum -=b;
        is_a_odd=a%2;
        if(is_a_odd)
        {
            sum -=a;
        }
    }
    s_even = (sum -3)/2 +2; // sum of the even sequence is 1 more than that of the odd one.
    printf("The total of the even numbers is %d\n",s_even);
    return 0;
}
