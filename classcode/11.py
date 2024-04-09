'''
Interface
'''

print(12e12)
print(repr(12e12))

print(repr(min))
'''
repr : python read
str  : human read

'''
from fractions import Fraction
half = Fraction(1,2)
print(repr(half))
print(str(half))
print(half.__repr__())

print('------------------')
from math import gcd

class Ratio:
    def __init__(self,n,d) -> None:
        self.numer = n
        self.denom = d
    
    def __repr__(self):
        return 'Ratio({0},{1})'.format(self.numer,self.denom)
    
    def __str__(self) -> str:
        return '{0}/{1}'.format(self.numer,self.denom)
    
    def __add__(self,other):
        if isinstance(other,int):
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other,float):
            return float(self) + other
        elif isinstance(other,Ratio):
            n = self.numer * other.denom + self.denom*other.numer
            d = self.denom*other.denom
      

        g = gcd(n,d)
        return Ratio(n//g , d//g)
    
    def __float__(self):
        return self.numer / self.denom



half = Ratio(1,2)
print(half)

print(Ratio(1,2) + Ratio(1,3))
print(Ratio(1,2) + 1)
print(Ratio(1,2) + 0.5)