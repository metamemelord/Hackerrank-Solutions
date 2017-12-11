# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:15:29 2017

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
