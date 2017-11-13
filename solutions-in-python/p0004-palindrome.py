'''         Problem 4. A palindrome
                
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
#
#global variables
MAX_N_OF_P_FACTORS=10
MAX_N_OF_FACTORS=200
FACTOR_COL=0; EXP_COL=1;

def palindrome(): ## This is the main function
    n_of_digits=6
    n_of_digits_of_f=3
    maximum=10**n_of_digits_of_f-1
    minimum=10**(n_of_digits_of_f-1)
    upper_limit=998001
    factor_found=0
    
    while(not factor_found):
        pal_number=g_palindrome(n_of_digits, upper_limit)
        factors=[1 for i in range(MAX_N_OF_FACTORS)]
        n_of_factors=factorize(pal_number,factors)
        i=-1
        while((not factor_found)and(i<n_of_factors-1)):
            i+=1
            if(minimum<=factors[i]<=maximum):
                pair=pal_number//factors[i]
                if(minimum<=pair<=maximum):
                    factor_found=1
        upper_limit=pal_number-1

def factorize(to_be_factorized, factor_array):
    p_factors=[[0]*2 for i in range(MAX_N_OF_P_FACTORS)]
    n_of_factors=1; place_in_array=0
    
    n_of_p_factors=factorize_in_prime(to_be_factorized, 3, p_factors)
    for i in range(n_of_p_factors):
        n_of_factors *= (p_factors[i][EXP_COL]+1)
    
    k=n_of_factors
    for p in range(n_of_p_factors):
        n_of_loops=n_of_factors//k
        k=k//(p_factors[p][EXP_COL]+1)
        for t in range(n_of_loops):
            for i in range(p_factors[p][EXP_COL]+1):
                for j in range(k):
                    place_in_array = k*(p_factors[p][EXP_COL]+1)*t+k*i+j
                    factor_array[place_in_array] *= p_factors[p][FACTOR_COL]**i
    return n_of_factors
    
def factorize_in_prime(factorized, n_digits, p_factor_array):
    N=factorized; f_part=1
    i=0; factor_in_range=0;
    minimum=pow(10,n_digits-1)
    maximum=pow(10,n_digits)-1
    for divisor in range(2, N):
        not_divided=N%divisor
        while not not_divided:
            if(p_factor_array[i][FACTOR_COL]!=divisor):
                if(p_factor_array[i][EXP_COL]>0):
                    i+=1
                p_factor_array[i][FACTOR_COL]=divisor
            p_factor_array[i][EXP_COL]+=1
            
            N=N//divisor
            ## This is to find a pair of factors in range.
            f_part*=divisor
            if(minimum<=f_part<=maximum and minimum<=N<=maximum):
                factor_in_range = f_part
            ##
            not_divided=N%divisor
    n_of_p_factors=i+1
    return n_of_p_factors

def g_palindrome(num_of_digits, maximum):
    digits=[0 for i in range(num_of_digits)]
    number=maximum
    print("The given number:\t",number)
    for i in range(num_of_digits):
        digits[i]=number//10**(num_of_digits-i-1)
        number-=digits[i]*10**(num_of_digits-i-1)
    
    # Find the digit which can be borrowed
    num_of_digits_is_odd=num_of_digits%2
    if(num_of_digits_is_odd):
        i=num_of_digits//2
    else:
        i=num_of_digits//2-1
    
    borrowed=-1
    while (borrowed<0):
        if (digits[i]):
            borrowed=i
        i-=1
    
    i=0
    borrow_f=0
    pair=num_of_digits-1
    while(i<num_of_digits):
        if(i==borrowed and borrow_f):
            digits[i]-=1
        while((not digits[i])and(borrowed<i<num_of_digits-borrowed-1)and(borrow_f)):  
            digits[i]=9
            i+=1
            pair-=1
        if(digits[i]>digits[pair]):
            if(i<pair):
                digits[pair]=digits[i]
                borrow_f=1
            else:
                digits[i]=digits[pair]
        elif(digits[i]<digits[pair]):
            if(i<pair):
                digits[pair]=digits[i]
        i+=1
        pair-=1
        
    for i in range(num_of_digits):
        number+=digits[i]*(10**(num_of_digits-i-1))
    print ("The palindrome number:\t",number)
    return number

# Calling the main function
if __name__ == "__main__":
    palindrome()
