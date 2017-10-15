# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

"""
q = int(input())
while q>0:
    q -= 1
    n = int(input())
    s = bin(n)
    s = s[2:]
    count = 0
    for i in range(len(s)):
        if s[i] == '0':
            count += 2**(len(s[i:])-1)
    print(count)
"""

for _ in range(int(input()))
    n = int(input())
    print((1<<n.bit_length())-n-1)
