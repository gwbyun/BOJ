#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 20:23:46 2022

@author: gw
"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x== k:
            print(dist[x])
            break
        for nx in (x-1,x+1,x * 2):
            if 0<=nx <=max:
                if dist[nx] ==0:
                    dist[nx] = dist[x] + 1 #dist의 요소값 = 시간(깊이). dist의 위치값 = 위치
                    q.append(nx)
            
max = 100000
dist = [0] * (max + 1)
n ,k = map(int,input().split())

bfs()