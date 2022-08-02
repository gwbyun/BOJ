#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 19:05:38 2022

@author: gw
"""

n,k = map(int, input().split())

worth = []
for i in range(n):
    worth.append(int(input()))
count =0
while k>=0:
    count += k//worth[n-1]
    k= k%worth[n-1]
    n -= 1
    if k == 0:
        print(count)
        break
    
    
    
    