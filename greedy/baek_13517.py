#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 12:09:41 2022

@author: gw
"""

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int,input().split()))

pivot=cost[0]
money = 0
for i in range(len(distance)):
    if pivot > cost[i]:
        pivot = cost[i]
    money = money + pivot * distance[i]
print(money)
'''
print(cost.index(min(cost)))
a=0
for i in (cost.index(min(cost)), len(distance)+1):
    a = a + min(cost) * distance[i] 
    '''