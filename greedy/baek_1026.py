#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 19:53:27 2022

@author: gw
"""

n = int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

pivot = sorted(b,reverse = True)

a.sort()
add = 0
for i in range(n):
    
    add += a[i]* pivot[i]
print(add)