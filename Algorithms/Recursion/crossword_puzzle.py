# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:47:51 2017

@author: MetaMemeLord-
"""
blanks = []
fin_board = []

x = [input() for _ in range(10)]
cities = input().strip(' ').split(';')

def init():
    for i in range(10):
        r,c = [],[]
        for j in range(10):
            if x[i][j]=='-':
                r.append((i,j))
            elif len(r)==1:
                r=[]
            elif len(r)>1:
                blanks.append(r)
                r=[]
            if j==9 and len(r)>1:
                blanks.append(r)
                r=[]
            if x[j][i]=='-':
                c.append((j,i))
            elif len(c)==1:
                c=[]
            elif len(c)>1:
                blanks.append(c)
                c=[]
            if j==9 and len(c)>1:
                blanks.append(c)
                c=[]

def solve(xboard,xblanks,xcities):
    global fin_board
    if len(xblanks)==0:
        fin_board = xboard
    else:
        for t in xblanks:
            for city in xcities:
                if len(city)==len(t) and all(xboard[t[i][0]][t[i][1]]=='-' or xboard[t[i][0]][t[i][1]]==city[i] for i in range(len(t))):
                    nboard=xboard[:]
                    for i in range(len(t)):
                        tboard = list(nboard[t[i][0]])
                        tboard[t[i][1]] = city[i]
                        nboard[t[i][0]] = ''.join(tboard)
                    nblanks = xblanks[:]
                    nblanks.remove(t)
                    ncities=xcities[:]
                    ncities.remove(city)
                    solve(nboard,nblanks,ncities)
init()
solve(x,blanks,cities)
for row in fin_board:
    for i in row:
        print(i,end='')
    print()
