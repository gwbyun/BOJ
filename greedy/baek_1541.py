#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 20:20:44 2022

@author: gw
"""

a = input().split()
num=[]
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1,len(num)):
    n -= num[i]
print(n)