# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

import itertools
n,m = map(int,input().strip().split())
klist=[]
for i in range(n):
    klist.append(int(input(),2))
mx = -float('inf')
t=0
for p1,p2 in itertools.combinations(range(n),2):
    topics = bin(klist[p1]|klist[p2]).count('1')
    if (topics==mx):
        t+=1
    elif (topics>mx):
        mx = topics
        t=1

print(mx,t,sep='\n')
