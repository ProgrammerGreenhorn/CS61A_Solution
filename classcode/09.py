'''
Generator Function m
                  -- a function that yields values instead of returning them
'''


def plus_minus(x):
    yield x
    yield -x

t = plus_minus(3)
print(t)
print(next(t))
print(next(t))

'''
return the evens between start and end
'''
def evens(start,end):
    even = start + (start % 2)
    while even < end:
        yield even
        even+=2

print(list(evens(1,10)))