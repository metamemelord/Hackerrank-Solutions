# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
for i in range(int(input())):
    n = str(bin(int(input())))
    n = n[2:]
    n = ''.join(reversed(n))
    for i in range(len(n),32):
        n += '0'
    n = ''.join(reversed(n))
    s = ''
    for i in n:
        if i=='0':
            s += '1'
        else:
            s += '0'
    print(int(s,2))
