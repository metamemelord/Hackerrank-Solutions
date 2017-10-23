# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

n,e = map(int,input().split())
x = [[] for i in range(n)]
check = [True]*n

def eventree(n):
	global ans
	check[n] = False
	count = 0
	if(len(x[n]) == 1):
		return 1
	for i in x[n]:
		if check[i]:
			count += eventree(i)
	count += 1
	if(count %2 == 0 and count != 0):
		ans += 1
		return 0
	else:
		return count
while(e>0):
	e -= 1
	x1,y1 = map(int,input().split())
	x[x1-1].append(y1-1)
	x[y1-1].append(x1-1)
ans = 0
eventree(0)
print(eventree(0))
