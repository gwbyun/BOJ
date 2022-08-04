#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 19:13:48 2022

@author: gw
"""
import heapq

n = int(input())

lecture_list = [list(map(int,input().split())) for _ in range(n)]
lecture_list.sort()

#print(n,time)

lecture_queue = []
heapq.heappush(lecture_queue, lecture_list[0][1]) #시작이 가장빠른 수업 종료시간을 heapq에 넣음

for i in range(1,n):
    if lecture_list[i][0] < lecture_queue[0]: #빠른 수업시간의 종료시간과 다음 수업의 시작시간을 비교
        heapq.heappush(lecture_queue) #종료시간이 더 늦을경우 강의실 하나 더필요 힙큐에 넣는다
        heapq.heappush(lecture_queue, lecture_list[i][1])
    else:
        heapq.heappop(lecture_queue) #강의실 필요없는경우 힙큐에있던 시간 교체
        heapq.heappush(lecture_queue, lecture_list[i][1])
        
print(len(lecture_queue))