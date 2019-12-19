#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
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

        """GRAPH DISgitPLAY SETTINGS"""
        self.mast = self.figure.add_subplot(111)
        self.deck = self.figure.add_subplot(111)
        self.mast.add_patch(Rectangle((-10, -800), 30, 1303, linewidth=1, edgecolor='#95634a', facecolor='#95634a', zorder=2))
        self.deck.add_patch(Rectangle((-1510, -800), 3000, 10, linewidth=1, edgecolor='#95634a', facecolor='#95634a'))
        self.sail = self.figure.add_subplot(111)
        self.hull = self.figure.add_subplot(111)
        self.sea = self.figure.add_subplot(111)
        self.sea.add_patch(Rectangle((-2150, -900), 4500, -1060, linewidth=1, edgecolor='blue', facecolor='blue', zorder=3, alpha=0.5))
        self.graph = Graph(self.sail)

        """DIMENSIONS INITIALIZATION"""
        self.input = InputReader()
        self.box = Box(200, 1000, -600, 200)
        self.wind = Wind(self.box)
        self.windType = 1
        self.windTime = 0

        """MATHEMATICAL OBJECTS INITIALIZATION"""
        self.sail_bezier = Bezier(
            min(self.box.get_x_range()),
            min(self.box.get_y_range()),
            0, -500,
            0, 500,
            True
        )

        self.hull_bezier = Bezier(
            -700, -1600,
            -1500, -800,
            1490, -800
        )
        self.hull_bezier.compute_bezier_curve()
        self.hull.plot(
            self.hull_bezier.control_point_matrix[0],
            self.hull_bezier.control_point_matrix[1],
            '#95634a', linewidth=2)
        self.hull.fill_between(self.hull_bezier.control_point_matrix[0], -800, self.hull_bezier.control_point_matrix[1], facecolor='#95634a')

        self.line, = self.graph.ax.plot(
            self.sail_bezier.control_point_matrix[0],
            self.sail_bezier.control_point_matrix[1],
            '#ffffff', zorder=1)

    def animate(self, i):
        """UPDATE WIND"""

        if self.windType == 1:
            self.windTime += 1
        else:
            self.windTime -= 1

        if self.windTime >= 1000:
            self.windType = 2
        elif self.windTime == 0:
            self.windType = 1

        self.update_wind(self.windType)

        """UPDATE CONTROL POINT POSITION"""
        self.sail_bezier.set_control_point(
            self.box.update_x(self.sail_bezier.base_control_point_x, self.wind.x_counter),
            self.box.update_y(self.sail_bezier.base_control_point_y, self.wind.y_counter))
        self.sail_bezier.compute_bezier_curve()
        """UPDATE GRAPH COORDINATES"""
        self.line.set_xdata(self.sail_bezier.control_point_matrix[0])
        self.line.set_ydata(self.sail_bezier.control_point_matrix[1])
        return self.line,

    def update_wind(self, wind_type):
        if wind_type == 1:
            self.wind.rising_storm()
        elif wind_type == 2:
            self.wind.calm_water()
