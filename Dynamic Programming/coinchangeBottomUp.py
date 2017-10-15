# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

def ans(n,c):
	dp = [0] * (n+1)
	dp[0] = 1
	for i in c:
		for j in range(1,len(dp)):
			if j >= i:
				dp[j] += dp[j-i]
	return dp[n]
n,m = map(int,input().split())
c = list(map(int, input().strip().split(' ')))
print(ans(n,c))
