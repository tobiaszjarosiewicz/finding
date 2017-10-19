#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:36:05 2017

Finding element similar to <X>

@author: tjarosiewicz
"""

from scipy import spatial
import numpy as np
import math
import time


def printmax(twodar, N):
    """
    For printing matrix in a visually correct order.
    """
    for x in range(N):
        for y in range(N):
            print(twodar[x][y], end="")
        print("")

def make_coordinates(N):
    """
    Probably useless.
    """
    points = []
    for i in range(N):
        for j in range(N):
            cord = (i, j)
            points.append(cord)
    return points
    
N = 3

A = np.random.random((N, N, 1))*100

print(A.shape)
print(A.ndim)
#print(A)
printmax(A, N)

#"""
# First approach of finding nearest value to pt:
ts1 = time.clock()
pt = [0]

#f = A[spatial.KDTree().query(pt)[1]]

points = make_coordinates(N)
tree = spatial.KDTree(points)
f = tree.query_ball_point([1, 1], 2)

tf1 = time.clock()
print("spatial: {}".format(f))
#print(tf1-ts1)


#"""
