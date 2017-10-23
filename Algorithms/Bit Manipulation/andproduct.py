# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

for _ in range(int(input())):
    a,b = map(int,input().split())
    al,bl = list(bin(a)[2:]),list(bin(b)[2:])
    if a==0:
        print(0)
        continue
    if len(al)!=len(bl):
        print(1<<len(bl-2))
    else:
        count = 0
        val = 0
        check = True
        s = ''
        for i in range(len(al)):
            if al[i] != bl[i]:
                break
            else:
                s += str(al[i])
        while i<len(al):
            s += '0'
            i += 1
        print(int(s,2))
