# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

def check(s):
	m = 'abcdefghijklmnopqrstuvwxyz'
	i = 0
	j = 0
	while(i<26  and j<len(s)):
		if(s[j] == m[i]):
			i += 1
		j+=1
	if(i==26):
		return True
	else:
		return False

s = input().strip()
if(check(''.join(sorted(s.lower())))):
    print('pangram')
else:
    print('not pangram')
