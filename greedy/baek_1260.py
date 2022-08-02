#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:17:35 2022

@author: gw
"""

import sys
from collections import deque
#input=sys.stdin.readline

n,m,start=map(int,input().split())
visited=[False]*(n+1)

graph=[[] for _ in range(n+1)]


for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()
    
def dfs(start):
    print(start,end = '')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            visited[i] = True
            
def bfs(start):
    q= deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        print(now,end='')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

dfs(start)
visited=[False]*(n+1)
print()
bfs(start)