#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 20:55:44 2022

@author: gw
"""
n,m = map(int,input().split())
A=[]
B=[]
cnt = 0
for i in range(n):
    A.append(list(map(int,input())))
for i in range(n):
    B.append(list(map(int,input())))
#print(A)
def flip(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            A[x][y]= 1-A[x][y]
            
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            flip(i,j)
            cnt +=1
            
        if A==B:
            break
    if A==B:
        break
    
if A != B:
    print(-1)
else:
    print(cnt)
        