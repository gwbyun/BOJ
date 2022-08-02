#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 21:44:25 2022

@author: gw
"""
from collections import deque

n = int(input())
graph = [list(map(int,list(input()))) for _ in range(n)]

def bfs(graph,x,y):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    return cnt
count = [bfs(graph,i,j) for i in range(n) for j in range(n) if graph[i][j]==1]

count.sort()
print(len(count))

for i in range(len(count)):
    print(count[i])