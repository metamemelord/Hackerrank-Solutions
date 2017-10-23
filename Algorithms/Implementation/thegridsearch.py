# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 00:36:30 2017

@author: MetaMemeLord-
"""

def check(x,xs,row,col,rs,cs):
    k = x[row:row+rs]
    for i in range(len(k)):
        k[i] = k[i][col:col+cs]
    #print(k)
    if k==xs:
        return True
    else:
        return False
#ans = []
q = int(input())
while q>0:
    r,c = map(int,input().split())
    x = []
    xs = []
    for i in range(r):
        x.append(input())
        assert len(x[i])==c,quit()
    rs,cs = map(int,input().split())
    if rs>r or cs>c:
        quit()
    for i in range(rs):
        xs.append(input())
        assert len(xs[i])==cs,quit()
    test = True
    for i in range(r):
        if r-i < rs:
            break
        else:
            ic = 0
            ib = 0
            ec = 0
            eb = 0
            while ib<c and ic<cs:
                if x[i][ib] == xs[0][ic] and x[i+rs-1][eb] == xs[rs-1][ec]:
                    ib += 1
                    eb += 1
                    ic += 1
                    ec += 1
                else:
                    ib += 1
                    eb += 1
                    if rs==r:
                        ec = 0
                        ic = 0
                #print(i,x[i],x[i+rs-1],xs[0],xs[rs-1])\
            if ic==cs and ec==cs:
                gridrow = i
                gridcol = ib-ic
                if check(x,xs,gridrow,gridcol,rs,cs):
                    print('YES')
                    #ans.append('YES')
                    test = False
                    break;
    if test:
        #ans.append('NO')
        print('NO')
    q -= 1
#print(ans)
