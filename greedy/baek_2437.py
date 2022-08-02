#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:26:30 2022

@author: gw
"""

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
target=1

for num in arr:
    if target < num:
        break
    
    target = target + num

print(target)