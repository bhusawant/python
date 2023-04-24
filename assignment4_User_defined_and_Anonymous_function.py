# Q.1


# def add_iter(*args):
#     """This function add the iterable objects. If give empty List so, you will get output 0"""
#     s=[]
#     total=0
#     for i in args:
#         s+=i
#         for element in range(0, len(s)):
#             total += s[element]
    
#     return total

# a = add_iter([10, 30], [10])

# print(a)


"""
# Q.1) sum of iterables pass as parameters
def sum_iterable(*args):
    s=0
    for iterable in args:
        if type(iterable)==dict:
            for item in iterable:
                s+=iterable[item]
        else:
            for item in iterable:
                s+=item
    return s

a = sum_iterable([10, 30], [10])
# a = sum_iterable({5:2},{4:2})
# a = sum_iterable([10, 30])
# a = sum_iterable([])
# a=sum_iterable({2:12, 3:4, 5:6})

print(a)
"""
       

"""
# Q.2) Moving average of given list

import numpy as np
def average1(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n-1:]/n

a = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
print(average1(a, n=3))
"""


# Q.3) Program to convert 1D array to vandermonde matrix

import numpy as np
M = np.array([1, 2, 3])
p=3
print(np.vander(M, p, increasing= True))
print(np.vander(M, p, increasing= False))
