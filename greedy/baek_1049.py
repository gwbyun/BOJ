#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 22:16:11 2022

@author: gw
"""

n,m = map(int,input().split())
graph=[]
cost = 0
for i in range (m):
    graph.append(list(map(int,input().split())))
    
if n==6:
    cost = min(min(graph[:][0]),6*min(graph[:][1]))
else:
    cost = n*min(graph[:][1])
    
print(cost)
print(graph)
print(graph[1][0])
    
    