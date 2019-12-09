#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:18:19 2019
@author: danidani
"""

from root import Root
from bezier import Bezier
import matplotlib.animation as animation
import matplotlib.pyplot as plt


# For testing purposes only
def ask_parameter(param):
    try:
        param_sail = int(input("Saisissez " + param + " du point de contrôle: "))
        return param_sail
    except ValueError:
        print("Veuillez saisir un entier")
        return ask_parameter()


root = Root(Bezier(ask_parameter("abscisse"), ask_parameter("ordonnée")))
ani = animation.FuncAnimation(root.figure, root.animate, interval=50)
root.mainloop()
