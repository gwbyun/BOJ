#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 23:25:53 2022

@author: gw
"""

n, k = map(int,input().split())
graph=[]
bag=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(k):
    a=int(input())
    bag.append(a)
print(graph)
print(bag)
graph.sort(reverse = True)
graph.sort(key=lambda x : -x[1])
