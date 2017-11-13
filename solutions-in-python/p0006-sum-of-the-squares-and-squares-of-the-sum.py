'''
Problem 6.
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
maximum=100
s=0
for i in range(2,maximum+1):
    partial_s=0
    for j in range(1,i):
        partial_s+=j
    s+=partial_s*i
difference=2*s
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is",difference)
