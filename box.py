#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Box:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.x_interval = [self.x_min, self.x_max]
        self.y_interval = [self.y_min, self.y_max]

    def in_x_interval(self, x):
        return self.x_min < x < self.x_max

    def in_y_interval(self, y):
        return self.y_min < y < self.y_max

    def update_x(self, old_x, new_x):
        if self.x_min < new_x < self.x_max:
            return new_x
        else:
            return old_x

    def update_y(self, old_y, new_y):
        if self.y_min < new_y < self.y_max:
            return new_y
        else:
            return old_y
