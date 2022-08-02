#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 00:05:22 2022

@author: gw
"""
def factorial(n):
    if n==1 or n==0:
        return 1
    return n * factorial(n-1)

print(factorial(10))