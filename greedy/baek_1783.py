#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 14:12:25 2022

@author: gw
"""

N, M = map(int, input().split())
if N == 1:
    scount = 1
elif N == 2:
    scount = min(4, (M-1)//2 + 1)
elif M < 7:
    scount = min(4, M)
else:
    scount = (2 + (M-5)) + 1
print(scount)
