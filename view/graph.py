#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Graph:
    def __init__(self, axis):
        self.ax = axis
        self.ax.axis([-2160, 2160, -1880, 1000])
        self.ax.set_facecolor('#3399ff')
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
