# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
t = int(input().strip())
for a0 in range(t):
	n,k = input().strip().split(' ')
	n,k = [int(n),int(k)]
	ontimecount = 0
	a = [int(a_temp) for a_temp in input().strip().split(' ')]
	for i in a:
		if(i<=0):
			ontimecount += 1
	if(k>ontimecount):
		print('YES')
	else:
		print('NO')
