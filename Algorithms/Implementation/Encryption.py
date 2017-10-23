# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

import math

s = ''.join(input().split())
length = len(s)
row = math.floor(math.sqrt(length))
col = row
check = True
while row*col < length:
    if check:
        check = False
        row += 1
    else:
        col += 1
#print(row,col)
i = 0
while i<row:
    k = i
    i += 1
    while k<length:
        print(s[k],end='')
        k += row
    print(' ',end='')
