# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
n,k = (int(x) for x in input().split())
c = [int(x) for x in input().split()]
E = 100
i = 0
while(E>0):
	E -=1
	if c[i]:
		E -= 2
	i += k
	i = i%n
	if(i==0):
		break
print(E)
