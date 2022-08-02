#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:41:44 2022

@author: gw
"""

def dfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        nx= x + dx[i]
        ny= y + dy[i]
        if (0<=nx<n) and (0<=ny<m):
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = -1
                dfs(nx,ny)
                
T = int(input())

for _ in range(T):
    m,n,k = map(int,input().split())
    matrix = [[0]*m for _ in range(n)]
    cnt = 0
    
    for _ in range(k):
        M,N = map(int,input().split())
        matrix[n][m] = 1
        
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dfs(i,j)
                cnt +=1
print(cnt)
        
