#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 17:10:39 2022

@author: gw
"""

n = int(input())
p=list(map(int,input().split()))
time = 0
p.sort(reverse=False)
print(p)
for i in range(5):
    #print(p[i])
    time = time + p[i] * (n-i)

print(time)