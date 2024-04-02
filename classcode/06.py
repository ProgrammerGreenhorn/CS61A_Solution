def count(s,value):
    '''Count the number of times that value in sequence s
    >>>count([1,2,1,2,1],1)
    3
    '''
    total = 0
    for element in s:
        if element == value:
            total+=1
    return total

pairs = [[1,2],[2,2],[3,2],[4,4]]

for x,y in pairs:
    print(x,y)


def sum_below(n):
    total = 0
    for i in range(n):
        total+=i
    return total

def cheer():
    for _ in range(3):
        print("Go Bears!")

"""
List Comprehension
"""
odds = [1,3,5,7,9]
[x + 1 for x in odds]

[x for x in odds if 25 % x == 0]


def divisors(n):
    return [1] + [x for x in range(2,n) if n % x == 0]


'''
Data Abstraction
'''
from math import gcd

def rational(n,d):
    '''Construct a rational number that represents N/D
    Keep the n and d relatively prime
    '''
    g = gcd(n,d)
    return [n//g,d//g]
    
def numer(x):
    return x[0]

def denom(x):
    return x[1]

def mul_rational(x,y):
    return rational(numer(x)*numer(y),denom(x)*denom(y))

def add_rational(x,y):
    return rational(numer(x)*denom(y) + numer(y)*denom(x),denom(x)*denom(y))

def equal_rational(x,y):
    return numer(x)*denom(y) == numer(y)*denom(x)
 
def print_rational(x):
    print(numer(x),'/',denom(x))


