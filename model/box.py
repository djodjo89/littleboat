#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Box:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_range = range(x_min, x_max)
        self.y_range = range(y_min, y_max)

    def get_x_range(self):
        return self.x_range

    def get_y_range(self):
        return self.y_range

    def update_x(self, old_x, new_x):
        return new_x if new_x in self.x_range else old_x

    def update_y(self, old_y, new_y):
        return new_y if new_y in self.y_range else old_y
