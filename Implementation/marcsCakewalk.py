# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
c = 0
n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
calories.sort()
length = len(calories)
for i in range(length):
	c += (2**i)*calories[length-i-1]
print(c)
