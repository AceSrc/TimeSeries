#!/bin/env python3

def Euclid(a, b):
    rt = 0
    n = len(a)
    for i in range(n):
        rt = (a[i] - b[i]) * (a[i] - b[i])
    return rt