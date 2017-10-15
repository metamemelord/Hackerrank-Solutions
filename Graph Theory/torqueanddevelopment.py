# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

def dfs(x,c,done):
	done[c] = False
	count = 0
	check = False
	for i in x[c]:
		if done[i]:
			check = True
			count += dfs(x,i,done)
	if not check:
		return 1
	return count+1

for i in range(int(input())):
	c,r,cl,cr = map(int,input().split())
	done = [True]*c
	x = [[] for i in range(c)]
	for p in range(r):
		i,j = map(int,input().split())
		x[i-1].append(j-1)
		x[j-1].append(i-1)
	sum = 0
	for i in range(c):
		if done[i]:
			val = 1000000000000000000000
			length = dfs(x,i,done)
			for j in range(1,length+1):
				val = min(j*cl + (length-j)*cr,val)
			sum += val
	print(sum)
