# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

for _ in range(int(input())):
    w,b = (int(x) for x in input().split())
    cw,cb,cc = (int(x) for x in input().split())
    if cc+cw<cb:
        print(w*cw + (cc+cw)*b)
    elif cc+cb<cw:
        print(w*(cb+cc) + b*cb)
    else:
        print(w*cw + b*cb)
