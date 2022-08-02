#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 14:59:05 2022

@author: gw
"""

#bfs

n = int(input())
m=int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] *(n+1)

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph,i,visited)
    return True

dfs(graph,1,visited)
print(sum(visited)-1)