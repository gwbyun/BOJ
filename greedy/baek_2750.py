#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 23:15:27 2022

@author: gw
"""

n = int(input())
graph = []
for i in range(n):
    graph.append(int(input()))
    
graph.sort(reverse = False)
for i in graph:
    print(i)
    