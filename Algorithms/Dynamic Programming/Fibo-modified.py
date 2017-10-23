# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

checked = []

def _init(n):
    for x in range(0,n+1):
        checked.append(0)

def modfib(first,second,pos):
    if(checked[pos]):
        return checked[pos]
    elif(pos == 0):
        checked[0] = first
        return first
    elif(pos == 1):
        checked[1] = second
        return second
    else:
        val = modfib(first,second,pos-2) + modfib(first,second,pos-1) * modfib(first,second,pos-1)
        checked[pos] = val;
        return val

f,s,n = map(int,input().split())
_init(n)
print(modfib(f,s,n-1))
