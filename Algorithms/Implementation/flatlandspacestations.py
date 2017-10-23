# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:23:02 2017

@author: MetaMemeLord-
"""
def binSearch(x,val):
    l = 0
    r = len(x)-1
    while l <= r:
        mid = (l + r)//2;
        if x[mid] == val:
            return True
        elif x[mid] < val:
            l = mid + 1
        else:
            r = mid - 1
    return False

def modifiedBin(x,val):
    l = 0
    r = len(x)-1
    while l <= r:
        mid = (l + r)//2;
        if x[mid] < val:
            l = mid + 1
        else:
            r = mid - 1
    return min(abs(val-x[r]),abs(val-x[l]))

def returnNearest(x,val):
    if val < x[0]:
        return abs(val-x[0])
    elif val > x[len(x)-1]:
        return abs(val-x[len(x)-1])
    else:
        return modifiedBin(x,val)

n,k = map(int,input().split())
x = list(map(int, input().split()))
x.sort()
maxDist = -1
dist = [None]*n
for i in range(n):
    if binSearch(x,i):
        dist[i] = 0
    else:
        dist[i] = returnNearest(x,i)
print(max(dist))
