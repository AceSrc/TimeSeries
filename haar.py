#!/bin/env python3

def HAAR(s, order):
    n = 2 ** order
    s = s + [0] * (n - len(s))
    rt = [0] * n
    for step in range(order, 0, -1):
        N = 2 ** (step - 1)
        for i in range(0, N):
            rt[i + N] = s[2 * i] - (s[2 * i] + s[2 * i + 1]) / 2
        for i in range(0, N):
            s[i] = (s[2 * i] + s[2 * i + 1]) / 2
    rt[0] = s[0]
    return rt

def HAAR2CHAR(s, order):
    beta = [float('-inf'), -0.84, -0.25, 0.25, 0.84, float('inf')]

    rt = HAAR(s, order)
    n = len(rt)
    for i in range(n):
        for j in range(0, 5):
            if rt[i] > beta[j] and rt[i] <= beta[j]:
                rt[i] = j
                break
    return rt

if __name__ == '__main__':
    print(HAAR([9, 7, 3, 5], 2))
    print(HAAR([7, 3, 5, 1, 8], 3))
    print(HAAR([7, 3, 5, 1, 8, 8], 3))