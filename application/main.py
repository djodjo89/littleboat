#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:18:19 2019
@author: danidani
"""
from controller.root import Root
import matplotlib.animation as animation

if __name__ == '__main__':
    root = Root()
    ani = animation.FuncAnimation(root.figure, root.animate, interval=1)
    root.mainloop()
