# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
import sys
st = int(input())
arr = [int(x) for x in input().split()]
if(st!=len(arr)):
    sys.exit()
def fun(s):
   for i in range(1,len(s)):
     c = s[i]
     p = i
     while p>0 and s[p-1]>c:
         s[p]=s[p-1]
         p = p-1
     s[p]=c
     print(*[m for m in arr])
   return
fun(arr)
