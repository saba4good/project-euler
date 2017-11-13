'''
Problem 5.
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is divisible by all of the numbers from 1 to 20?
'''
PRM_COL=0;EXP_COL=1
upper_limit=20
primes=[]

for i in range(2, upper_limit+1):
    i_is_composite=0
    for j in range(2, i):
        if (not i%j):
            i_is_composite=1
    if(not i_is_composite):
        primes.append([i])
lcm=1
print("The prime numbers are:")
for prime in primes:
    exp=0
    number=upper_limit
    while(number>=prime[PRM_COL]):
        number=number//prime[PRM_COL]
        exp+=1
    prime.append(exp)
    print(prime[PRM_COL],":",prime[EXP_COL])
    for i in range(prime[EXP_COL]):
        lcm*=prime[PRM_COL]
print("The LCM:",lcm)
