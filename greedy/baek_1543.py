#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 19:39:01 2022

@author: gw
"""

s = input()
target = input()
result = 0
num =0

while num <= len(s)- len(target):
    if s[num:num+len(target)] == target:
        result +=1
        num+=len(target)
        
    else:
        num +=1
        
print(result)