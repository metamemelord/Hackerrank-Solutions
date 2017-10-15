# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

S = input().strip()
m = ''
for i in range(len(S)//3):
    m += 'SOS'
count = 0
for i in range(len(S)):
    if(S[i] != m[i]):
        count += 1
print(count)
