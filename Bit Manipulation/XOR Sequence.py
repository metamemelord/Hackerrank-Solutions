# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

def XOR(n):
    val=n%8
    if(val==0 or val==1):
        return n
    elif(val==2 or val==3):
        return 2
    elif(val==4 or val==5):
        return n+2
    else:
        return 0

t=int(input())
while t:
    t -= 1
    l,r=map(int,input().split())
    print(XOR(l-1)^XOR(r))
