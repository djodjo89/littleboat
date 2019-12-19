#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random as rand


class Bezier:
    def __init__(self, x, y, x_dir_p1, y_dir_p1, x_dir_p2, y_dir_p2, random=False):
        self.base_control_point_x = x
        self.base_control_point_y = y
        self.x_dir_p1 = x_dir_p1
        self.y_dir_p1 = y_dir_p1
        self.x_dir_p2 = x_dir_p2
        self.y_dir_p2 = y_dir_p2
        if random:
            self.control_point_matrix = np.array([[0, self.randomize_point_x(), 0], [0, self.randomize_point_y(), 6]])
        else:
            self.control_point_matrix = np.array([[0, self.base_control_point_x, 0], [0, self.base_control_point_y, 6]])

    def set_control_point(self, x, y):
        self.base_control_point_x = x
        self.base_control_point_y = y

    def randomize_point_x(self):
        return rand.randint(self.base_control_point_x - 1, self.base_control_point_x + 1)

    def randomize_point_y(self):
        return rand.randint(self.base_control_point_y - 1, self.base_control_point_y + 1)

    def compute_bezier_curve(self):
        self.control_point_matrix = np.array([[self.x_dir_p1, self.randomize_point_x(), self.x_dir_p2], [self.y_dir_p1, self.randomize_point_y(), self.y_dir_p2]])
        """ Number of points to display """
        n = 50
        mt = np.linspace(0, 1., n)
        matt = np.ones((3, n))
        matt[1, :] = mt
        matt[2, :] = mt * mt
        bezier_matrix_3 = np.array([
            [1, 0, 0],
            [-2, 2, 0],
            [1, -2, 1]
        ])
        point_matrix_line = np.dot(
            np.dot(
                matt.T,
                bezier_matrix_3
            ),
            self.control_point_matrix.T
        )
        self.control_point_matrix = point_matrix_line.T
