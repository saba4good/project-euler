'''
Problem 9.
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
a=0; i=1
while (not a and i<100):
    r_5=(1000*(100-i))%(200-i)
    r_2=(1000*(250-i))%(500-i)
    if not r_5:
        a=i*5
    elif not r_2:
        a=i*2
    i+=1
while (not a and i<250):
    r_2=(1000*(250-i))%(500-i)
    if not r_2:
        a=i*2
    i+=1

b=1000*(500-a)//(1000-a)
c=1000-a-b
mul=a*b*c
print("a:",a,"b:",b,"c:",c,"abc:",mul)
