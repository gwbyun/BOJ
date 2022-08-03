#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:52:37 2022

@author: gw
"""
import sys
from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
queue = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
res = 0

#m = x n =y

for i in range(n):
    for j in range(m):
        if matrix[i][j] ==1:
            queue.append([i,j])
            
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx <n:
                
                
bfs()

for i in matrix:
    for j in i:
        if j ==0:
            print(-1)
            
            