#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:18:19 2019
@author: danidani
"""
from box import Box
from root import Root
import matplotlib.animation as animation

sail_limits = Box(0, 15, 0, 5)
root = Root(sail_limits)
ani = animation.FuncAnimation(root.figure, root.animate, interval=1)
root.mainloop()
