# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

s = input()
i= 0
while i<(len(s)-1):
    if(s[i]==s[i+1]):
        s1 = s[0:i]
        s2 = s[i+2:len(s)]
        s = s1+s2
        i = 0
        continue;
    i += 1
if(len(s)!=0):
    print(s)
else: print('Empty String')
