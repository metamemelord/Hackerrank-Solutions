# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

for _ in range(int(input())):
    a,b = map(int,input().split())
    al,bl = list(bin(a)[2:]),list(bin(b)[2:])
    if a==0:
        print(0)
        continue
    if len(al)!=len(bl):
        print(1<<len(bl-2))
    else:
        count = 0
        val = 0
        check = True
        s = ''
        for i in range(len(al)):
            if al[i] != bl[i]:
                break
            else:
                s += str(al[i])
        while i<len(al):
            s += '0'
            i += 1
        print(int(s,2))
s = input().strip()
t = input().strip()
k = int(input().strip())
sl = len(s)
tl = len(t)
if s==t or ((k==2*sl) and sl==tl) or (k>sl+tl):
	print('Yes')
	quit()
for i in range(min(sl,tl)):
    if(s[i]!=t[i]):
        break
m = i
m+=1
if(m==min(sl,tl)):
	p = max(sl,tl) - m
	if(p!=0 and p%2 == 0 or (k-p)%2 == 0):
		print('Yes')
	else:
		print('No')
	quit()

i = sl+tl - 2*6
if (i==k):
	print('Yes')
	quit()
print('No')
