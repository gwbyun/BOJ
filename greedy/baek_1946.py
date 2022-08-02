#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:42:10 2022

@author: gw
"""
T = int(input())
graph = []
count = 1

for i in range(T):
    N = int(input())
    for j in range(N):
        graph.append(list(map(int,input().split())))
    a = sorted(graph, key = lambda x : x[0])
    pivot = a[0][1]
    #print(pivot)
    #print(graph)

    for i in range(1,N):
        if pivot >= a[i][1]:
            count += 1
            pivot = a[i][1]
               
    print(count)
   

   
