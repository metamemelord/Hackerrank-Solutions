# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
def kaprekar(n):
    k = str(n*n)
    if len(k) == 1:
        return n == int(k)
    index = len(k)//2
    try:
        right = int(k[index:])
    except:
        right = 0
    left = int(k[:index])
    if right == 0:
        return False
    if n == right + left:
        return True
    else:
        return False
s = int(input())
e = int(input())
check = True
for i in range(s,e+1):
    if kaprekar(i):
        check = False
        print(i,end=' ')
if check:
    print('INVALID RANGE')
