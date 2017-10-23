# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

import re

def test(s,size):
    if s.count('_') == 0 and len(re.sub(r'((.)\2+)', '', s)) != 0:
        return 'NO'
    for i in set(s):
        if i != "_" and s.count(i) == 1:
            return 'NO'
    return 'YES'

for _ in range(int(input())):
    n = int(input())
    s = input()
    assert n == len(s), quit()
    print(test(s,n))
