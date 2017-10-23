# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

def check(s):
    l = len(s)
    if(l>1):
        a = s[0]
        b = s[1]
        k = l//2

    if((len(set(s[::2]))==1 and len(set(s[1::2]))==1) and set(s[::2])!=set(s[1::2])):
            return True
    elif(l == 1): return False
    elif(l == 0): return True
    else: return False

def remove(s,char1,char2, string):
    for i in s:
        if(i!=char1 and i!=char2):
            string = string.replace(i,"")
    return string

l_max = 0
s_len = int(input().strip())
s = input().strip()
ss = list(set(s))
for i in range(0,len(ss)):
    for j in range(i,len(ss)):
        t = remove(ss,ss[i],ss[j],s)
        if(check(t)):
            l_max = max(l_max,len(t))
print(l_max)
