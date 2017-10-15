# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 02:23:32 2017

@author: MetaMemeLord-
"""

MOD = 1000000007
t = input()
s = [0]*len(t)
s[0] = int(t[0])
for i in range(1,len(t)):
    s[i] = (s[i-1]*10 + (i+1)*int(t[i]))%MOD
print(sum(s)%MOD)