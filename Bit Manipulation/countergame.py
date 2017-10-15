# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

for i in range(int(input())):
    print('Richard') if str(bin(int(input())-1)).count('1')%2 == 0 else print('Louise')
