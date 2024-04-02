def invert(x):
    y = 1/x
    print('Never printed if x is 0')
    return y

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('handled',e)
        return 0
    
from operator import add,mul,truediv

def reduce(f,s,initial):
    '''Combine elements of s using f starting with initial

    >>> reduce(mul,[2,4,8],1)
    64
    >>> reduce(add,[1,2,3,4],0)
    10
    
    '''
    for element in s:
        initial = f(initial,element);
    return initial

def reduce_recursive(f,s,initial):
    '''Combine elements of s using f starting with initial

    >>> reduce(mul,[2,4,8],1)
    64
    >>> reduce(add,[1,2,3,4],0)
    10
    
    '''
    if not s:
        return initial
    else :
        first,rest = s[0],s[1:]
        return reduce(f,rest,f(initial,first))
    

def divide_all(n,ds):
    try :
     return reduce(truediv,ds,n)
    except  ZeroDivisionError:
        return float('inf') 
    


'''Trees'''
def tree(label,branches = []):
    for branch in branches:
        assert is_tree(branch),'branches must be tree'
    return [label] + list(branches)

def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)     

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left,right = fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])


def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        count= [count_leaves(b) for b in branches(t)]
        return sum(count)
    
def leaves(t):
    '''
    return a list containing the leaf labels of tree
    '''
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([s for s in leaves(t)],[])
    
def increment(t):
    '''
    return a tree linke t but with all labels increment
    '''
    return tree(label(t)+1,[increment(b) for b in branches(t)])

def print_tree(t,indent=0):
    print('  ' *indent + str(label(t)))
    for b in branches(t):
        print_tree(b,indent+1)