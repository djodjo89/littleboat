#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Root(Tk):
    def __init__(self, bezier):
        super(Root, self).__init__()
        self.title('Little Boat')
        self.minsize(640, 360)
        self.bezier = bezier
        self.figure = Figure()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.ax = self.figure.add_subplot(111)
        self.line, = self.ax.plot(self.bezier.control_point_matrix[0], self.bezier.control_point_matrix[1], 'k')
        self.canvas.get_tk_widget().grid(column=0, row=1)

    def animate(self, i):
        self.bezier.display_bezier()
        self.line.set_xdata(self.bezier.control_point_matrix[0])
        self.line.set_ydata(self.bezier.control_point_matrix[1])
        return self.line,
