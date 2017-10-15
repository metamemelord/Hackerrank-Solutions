# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
def check(s):
	m = 'hackerrank'
	i = 0
	j = 0
	while(i<10  and j<len(s)):
		if(s[j] == m[i]):
			i += 1
		j+=1
	if(i==10):
		return True
	else:
		return False

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    if(check(s)):
        print('YES')
    else:
        print('NO')
