#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from bezier import Bezier
from input_reader import InputReader
from wind import Wind


class Root(Tk):
    def __init__(self, box):
        """NOT SO IMPORTANT ZONE"""
        super(Root, self).__init__()
        self.title('Little Boat')
        self.minsize(640, 360)
        self.figure = Figure()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().grid(column=0, row=1)
        self.input = InputReader()
        self.box = box
        self.wind = Wind(self.box)
        """END OF NOT SO IMPORTANT ZONE"""

        """AXIS DEFINITION AND GRAPH SETTINGS"""
        self.ax = self.figure.add_subplot(111)
        self.ax.axis([-50, 50, -20, 20])
        self.ax.set_facecolor('#3399ff')
        self.bezier = Bezier(self.input.ask_parameter("abscisse du point de contrôle", self.box.x_min, self.box.x_max),
                             self.input.ask_parameter("ordonnée du point de contrôle", self.box.y_min, self.box.y_max))
        self.line, = self.ax.plot(self.bezier.control_point_matrix[0], self.bezier.control_point_matrix[1], '#ffffff')

    def animate(self, i):
        """UPDATE WIND"""
        self.wind.rising_storm()
        """UPDATE CONTROL POINT"""
        self.bezier.set_control_point(
            self.box.update_x(self.bezier.base_control_point_x, self.wind.x_counter),
            self.box.update_y(self.bezier.base_control_point_y, self.wind.y_counter))
        self.bezier.compute_bezier_curve()
        """DRAW CURVE"""
        self.line.set_xdata(self.bezier.control_point_matrix[0])
        self.line.set_ydata(self.bezier.control_point_matrix[1])
        return self.line,
