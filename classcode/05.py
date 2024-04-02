def fact(n):
    if n==0 or n== 1:
        return 1
    else:
        return n*fact(n-1)
    
def sum_digits(n):
    if n < 10:
        return n
    else:
        return sum_digits(n//10) + n % 10
    
def sum_digits_iter(n):
    digit_sum = 0
    while n  > 0:
        n,last = n//10,n%10
        digit_sum  += last
    return digit_sum

'''
check sum
mutual calling
'''    
def luhn_sum(n):
    if n < 10:
        return n
    else:
        return luhn_double_sum(n//10) + n % 10
    
def luhn_double_sum(n):
    digit = 2*(n%10)
    if n < 10:
        return sum_digits(digit)
    else:
        return sum_digits(digit) + luhn_sum(n//10)
    

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def cascade_shorter(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)

'''
inverse_cascade implemention
'''
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow = lambda n : f_then_g(grow,print,n//10)
shrink = lambda n : f_then_g(print,shrink,n//10)



'''
Tree recursion
'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

def count_partitions(n,m):
    if m == 0:
        return 0
    elif n < 0:
        return 0
    elif n == 0:
        return 1
    
    else:
     return count_partitions(n,m-1) + count_partitions(n-m,m)
    

'''
Implementing a function
'''

def remove(n,digit):
    '''Return all digits of non-negative N that are
    differnt from digit
    >>>remove(231,3)
    21
    >>>remove(243132,2)
    4313
    '''
    kept,digits_tracked = 0,0
    while n > 0:
        n,last = n//10,n%10
        if last != digit:
            kept = kept + last * pow(10,digits_tracked)
            digits_tracked = digits_tracked + 1

    return kept



