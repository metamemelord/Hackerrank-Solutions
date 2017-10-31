# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:29:54 2017

@author: MetaMemeLord-
"""

# gcc -c -IC:\Anaconda3\include -o kruskalMST.o kruskalMST.c
# gcc -shared -LC:\Anaconda3\libs -o kruskalMST.pyd kruskalMST.o -lpython36

import sys

sys.setrecursionlimit(1000010)

gkey = lambda n: n[2]

def find(node):
    if node == x[node]:
        return node
    else:
        x[node] = find(x[node])
        return x[node]

def union(n1,n2):
    if n1 == n2:
        return
    if n1>n2:
        n1,n2 = n2,n1
    x[n2] = n1

n,e = map(int,input().split())
x = [i for i in range(n)]
q = []
for _ in range(e):
    v1,v2,c = map(int,input().split())
    v1,v2 = v1-1,v2-1
    q.append([v1,v2,c])
q.sort(key=gkey)
ans = 0
while len(q)>0:
    k = q.pop(0)
    n1,n2 = find(k[0]),find(k[1])
    if n1 == n2:
        continue
    else:
        union(n1,n2)
        ans += k[2]
print(ans)
