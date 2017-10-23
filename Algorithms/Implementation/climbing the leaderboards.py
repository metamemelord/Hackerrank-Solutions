# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

n = int(input())
per = [int(x) for x in input().split()]
m = int(input())
s = [int(x) for x in input().split()]
p = []
p.append(per[0])
for i in per:
	if(i<p[len(p)-1]):
		p.append(i)
rank = len(p)+1
j = rank-2
i = 0
while(i<m and j>=0):
	if(p[j] <= s[i]):
		j    -= 1
		rank -= 1
	else:
		print(rank)
		i += 1
for k in range(i,m):
	print(rank)
