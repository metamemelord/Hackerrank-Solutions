# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

n,k = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
d = {}
for i in range(len(a)):
	d[i] = a[i]%k
m = list(d.values())
l = [0]*k
for i in m:
	l[i]+=1
count = 0
if(k%2==0):
	p = k//2
	if(l[k//2] != 0):
		count +=1
else:
	p = k//2+1
if(l[0] != 0):
	count +=1
for i in range(1,p):
	count += max(l[i],l[k-i])
print(count)
