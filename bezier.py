#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random as rand


class Bezier:
    def __init__(self, px, py):
        self.base_control_point_x = px
        self.base_control_point_y = py
        self.control_point_matrix = np.array([[0, self.randomize_point_x(), 0], [0, self.randomize_point_y(), 6]])

    def randomize_point_x(self):
        return rand.randint(self.base_control_point_x - 1, self.base_control_point_x + 1)

    def randomize_point_y(self):
        return rand.randint(self.base_control_point_y - 1, self.base_control_point_y + 1)

    def display_bezier(self):
        self.generate_matrix()
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

    def generate_matrix(self):
        self.control_point_matrix = np.array([[0, self.randomize_point_x(), 0], [0, self.randomize_point_y(), 6]])
