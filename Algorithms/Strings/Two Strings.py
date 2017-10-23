# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
def twoStrings(s1, s2):
    # Complete this function
    s = set(list(s1))
    for i in s2:
        if i in s:
            return "YES"
    return "NO"

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
