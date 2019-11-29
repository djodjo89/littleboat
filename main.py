#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:18:19 2019

@author: danidani
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Creation of drawing environment
"""

"""
Make a square in which it is possible to draw
"""
plt.axis('scaled')
"""
Delimit orthonormal
"""
size = 20
plt.xlim(-size-1, size+1)
plt.ylim(-size-1, size+1)

def display_point(matPoint):
    """ All coordinates on array first row """
    x = matPoint[0, :]
    """ All coordinates on array second row """
    y = matPoint[1, :]
    """ Draw points """
    plt.plot(x, y, 'k-')
def display_segment(p1, p2):
    matP = np.concatenate((p1,p2),1)
    display_point(matP, 'k-')
def display_bezier_quad(matControlPoint):
    """ Number of points to display """
    n = 50
    mt = np.linspace(0,1.,n)
    matt = np.ones((3,n))
    matt[1,:] = mt
    matt[2,:] = mt*mt
    matBezier3 = np.array([
            [1, 0, 0],
            [-2, 2, 0],
            [1, -2, 1]
            ])
    matPointLine = np.dot(
                np.dot(
                   matt.T,
                   matBezier3
                ),
                matControlPoint.T
            )
    matPoint = matPointLine.T
    display_point(matPoint)
    return matPoint             
                