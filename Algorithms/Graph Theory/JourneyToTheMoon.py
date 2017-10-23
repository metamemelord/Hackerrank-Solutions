# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:36:55 2017

@author: MetaMemeLord-
"""

import sys

sys.setrecursionlimit(1000000)

def allDone(k,done):
    for i in range(k,len(done)):
        if not done[i]:
            return i
    return -1
def dfs(x,index):
    if done[index]:
        return 0
    done[index] = True
    val = 1
    for i in x[index]:
        val += dfs(x,i)
    return val

n,e = map(int,input().split())
x = [[] for _ in range(n)]
for i in range(e):
    v1,v2 = map(int,input().split())
    x[v1].append(v2)
    x[v2].append(v1)
done = [False]*n
count = []
k = 0
while True:
    k = allDone(k,done)
    if k==-1:
        break
    count.append(dfs(x,k))
total = sum(count)
index = 0
ans = 0
while index < len(count):
    ans += (total - count[index])*count[index]
    total -= count[index]
    index += 1
print(ans)
