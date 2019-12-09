#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from wind import Wind


class Root(Tk):
    def __init__(self, bezier):
        super(Root, self).__init__()
        self.title('Little Boat')
        self.minsize(640, 360)
        self.bezier = bezier
        self.figure = Figure()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.ax = self.figure.add_subplot(111)
        self.ax.axis([-50, 50, -20, 20])
        self.ax.set_facecolor('#3399ff')
        self.line, = self.ax.plot(self.bezier.control_point_matrix[0], self.bezier.control_point_matrix[1], '#ffffff')
        self.canvas.get_tk_widget().grid(column=0, row=1)
        self.wind = Wind()
        self.wind.x_counter = self.bezier.base_control_point_x
        self.wind.y_counter = self.bezier.base_control_point_y

    def animate(self, i):
        self.wind.rising_storm()
        self.bezier.base_control_point_x = self.wind.x_counter
        self.bezier.base_control_point_y = self.wind.y_counter
        self.bezier.display_bezier()
        self.line.set_xdata(self.bezier.control_point_matrix[0])
        self.line.set_ydata(self.bezier.control_point_matrix[1])
        return self.line,
