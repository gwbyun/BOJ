#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:46:49 2022

@author: gw
"""

n = input()
count1 = 0

for i in range (len(n)-1):
    if not n[i]==n[i+1]:
        count1 += 1
#print(count1)
if count1%2 != 0:
    num = (count1//2)+1
else:
    num = (count1//2)
print(num)
    