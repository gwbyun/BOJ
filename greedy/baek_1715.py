#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 20:30:20 2022

@author: gw
"""
import heapq

n = int(input())
card=[]
pivot=0

for i in range(n):
    card.append(int(input()))
heapq.heapify(card)

while len(card) != 1:
    num1=heapq.heappop(card)  
    num2=heapq.heappop(card)
    Sum= num1+num2
    pivot += Sum
    heapq.heappush(card,Sum)
    
print(pivot)