# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:58:58 2017

@author: MetaMemeLord-
"""

n = int(input())
inf = 10
x = [[int(i) for i in input()] for _ in range(n)]
for i in range(1,n-1):
    for j in range(1,n-1):
        if x[i][j] > x[i+1][j] and x[i][j] > x[i-1][j] and x[i][j] > x[i][j+1] and x[i][j] > x[i][j-1]:
            x[i][j] = inf
for i in range(n):
    for j in range(n):
        if x[i][j] == 10:
            print('X',end='')
        else:
            print(x[i][j],end='')
    print()