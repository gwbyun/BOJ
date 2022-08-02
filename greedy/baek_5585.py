#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 10:16:27 2022

@author: gw
"""

n = int(input())
coin = [500, 100, 50, 10, 5, 1]
n = 1000-n
count = 0
for i in coin:
    count += n//i
    n = n%i
print(count)