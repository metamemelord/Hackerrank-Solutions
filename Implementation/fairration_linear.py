# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

n = int(input())
x = list(map(int,input().split()))
count = 0
for i in range(len(x)):
    if x[i]%2:
        if i == n-1:
            print('NO')
            break
        else:
            x[i+1] += 1
            count += 2
else:
    print(count)
