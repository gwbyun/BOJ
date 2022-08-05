#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 20:50:51 2022

@author: gw
"""

import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline()
#dfs로 그래프를 탐색－
def dfs(start, depth):
    # 시작점을 방문처리
    visited[start]= True
    
    for i in graph[start]:
        if not visited[i]:
            #0일경우 True출력
            dfs(i, depth+1)
            
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (1+n)
count = 0

for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            count +=1
            visited[i] = True
        else:
            dfs(i,0)
            count+=1
print(count)