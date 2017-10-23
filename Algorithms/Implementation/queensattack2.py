# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""

def check(board, r, c, dR, dC, n):
    sum = 0
    for i in range(n):
        r += dR
        c += dC
        if r < 0 or r >= n or c < 0 or c>=n:
            return sum
        key = str(r) + "-" + str(c)
        if key in board and board[key] == -1:
            return sum
        else:
            sum += 1
    return sum

n,k = map(int,input().split())
rq,cq = map(int,input().split())
rq -= 1
cq -= 1
cboard = {}
for _ in range(k):
    rObs,cObs = input().strip().split(' ')
    rObs,cObs = [int(rObs),int(cObs)]
    r = rObs - 1
    c = cObs - 1
    cboard[str(r) + "-" + str(c)] = -1
dCList = [ -1, -1 , -1, 0 , 0, 1 , 1 , 1]
dRList = [ -1 , 0 , 1, -1,  1, 0, -1, 1]
sum = 0
for i in range(8):
    sum += check(cboard, rq, cq, dCList[i], dRList[i], n)
print(sum)
