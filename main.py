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

"""
Creation of the method for bezier curve
"""

def visu_point(matPoint,style):
    # matPoint contains points coordinates
    x = matPoint[0, :]
    y = matPoint[1, :]
    plt.plot(x, y, style)


def visu_BezierQuad(matPointControl,str):
    
    n=50
    mt = np.linspace(0,1.,n)  
    matt = np.ones((3,n))  # only many 1
    matt[1,:] = mt  # line with many t
    matt[2,:] = mt*mt  # line with many t*t

    matBezier3 = np.array([[1, 0, 0], 
                           [-2, 2, 0], 
                           [1, -2, 1]])

    matPointligne = np.dot(np.dot(matt.T,matBezier3),matPointControl.T)
    #Transposition
    matPoint=matPointligne.T

    #Draw point of the curve
    visu_point(matPointControl,'b.')
    
    #Draw dot between extremities and control point
    #visu_point(matPointControl,'b:')
    
    #Draw segments
    visu_point(matPoint,str)
    
# For testing purposes only
def askXParameter():
    try:
        x = int(input("Saisissez l'abscisse du point de contrôle: "))
        return x
    except ValueError:
        print("Veuillez saisir un entier")
        return askXParameter()


"""
Creation of the sail
"""
#Sail without rotation or wind 
#P1 = (0,0), P2 = (0, 3), P3 = (0, 6)
P2x = askXParameter()
P2y = 3
matPointControl = np.array([[0,P2x,0],[0,P2y,6]])
visu_BezierQuad(matPointControl, 'b') 


