#!/bin/env python3

def PAA(s, n, w):
    beta = [float('-inf'), -0.84, -0.25, 0.25, 0.84, float('inf')]
    
    B = n // w
    rt = [0] * B
    for i in range(0, B):
        for j in range(i * B, i * B + B):
            rt[i] += s[j]
        rt[i] = w * rt[i] / n

        for j in range(0, 5):
            if rt[i] > beta[j] and rt[i] <= beta[j]:
                rt[i] = j
                break
    return rt
