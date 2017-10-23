# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
memo= {}
x = []
def dp(s,done,index):
    if index == len(x):
        return 0
    if done>s:
        return done - x[index]
    if done == s:
        return done
    else:
        return max(dp(s,done+x[index],index),dp(s,done,index+1))
t = int(input())
while(t>0):
    t -= 1
    n,s = map(int,input().split())
    x = [int(i) for i in input().split()]
    print(dp(s,0,0))
    memo = {}
