"""Generalization"""
from math import pi,sqrt

def area_square(r):
    return  area(r,1)

def area_circle(r):
    return   area(r,pi)

def area_hexagon(r):
    return   area(r,3 * sqrt(3) / 2)


def area(r ,shape_constant):
    assert r > 0,'A length must be positive'
    return r * r * shape_constant








def identity(k):
    return k

def cube(k):
    return pow(k,3)

def summation(n,term):
    """Sum the first N terms of a sequence

    >>> summation(5,cube)
    225
    """
    total , k = 0 , 1
    while k <=n :
        total , k = total + term(k), k + 1
    return total


def sum_naturals(n):
    """Sum the first N natural number

    >>> sum_naturals(5)
    15
    """

    return summation(n , identity)

def sum_cubes(n):
    """Sum  first N cubes of natural numbers

    >>> sum_cubes(5)
    225
    """
    return summation(n , cube)












def make_adder(n):
    """Return a function that takes a argument K abd return K + N
    
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7

    >>> make_adder(1)(2)
    3

    >>> make_adder(2000)(13)
    2013
    """
    def adder(k):
        return k + n
    return adder


def square(x):
    return x * x

def triple(x):
    return 3 *x

def compose1(f,g):
    def h(x):
        return f(g(x))
    
    return h


def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g



def curry2_lambda(f):
    return lambda f : lambda x :lambda y : f(x,y)