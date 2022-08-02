#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 19:49:47 2022

@author: gw
"""

n, l = map(int, input().split())
a = list(map(int,input().split()))
a.sort()
for i in a:
    for j in range (1,l):
        if i+j in a:

            a.remove(i+j)
print(len(a))