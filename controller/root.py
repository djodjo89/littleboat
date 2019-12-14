#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from model.bezier import Bezier
from model.box import Box
from controller.input_reader import InputReader
from model.wind import Wind
from view.graph import Graph


class Root(Tk):
    def __init__(self):
        """NOT SO IMPORTANT ZONE"""
        super(Root, self).__init__()
        self.title('Little Boat')
        self.minsize(640, 360)
        self.figure = Figure()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().grid(column=0, row=1)
        """END OF NOT SO IMPORTANT ZONE"""

        """GRAPH DISPLAY SETTINGS"""
        self.graph = Graph(self.figure.add_subplot(111))

        """DIMENSIONS INITIALIZATION"""
        self.input = InputReader()
        self.box = Box(0, 1000, -600, 200)
        self.wind = Wind(self.box)

        """MATHEMATICAL OBJECTS INITIALIZATION"""
        self.bezier = Bezier(min(self.box.get_x_range()), min(self.box.get_y_range()))
        self.line, = self.graph.ax.plot(
            self.bezier.control_point_matrix[0],
            self.bezier.control_point_matrix[1],
            '#ffffff')

    def animate(self, i):
        """UPDATE WIND"""
        #self.wind.rising_storm()
        self.wind.calm_water()
        """UPDATE CONTROL POINT POSITION"""
        self.bezier.set_control_point(
            self.box.update_x(self.bezier.base_control_point_x, self.wind.x_counter),
            self.box.update_y(self.bezier.base_control_point_y, self.wind.y_counter))
        self.bezier.compute_bezier_curve()
        """UPDATE GRAPH COORDINATES"""
        self.line.set_xdata(self.bezier.control_point_matrix[0])
        self.line.set_ydata(self.bezier.control_point_matrix[1])
        return self.line,
