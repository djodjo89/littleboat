#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy.random import rand


class Wind:
    def __init__(self, box):
        self.box = box
        self.x_counter = min(box.get_x_range())
        self.y_counter = min(box.get_y_range())
        self.state = 'increasing'
        self.x_strength = 10
        self.y_strength = 1

    def increase(self, x, y):
        self.set_counters(self.x_counter, self.y_counter, self.x_counter + x, self.y_counter + y)

    def decrease(self, x, y):
        self.set_counters(self.x_counter, self.y_counter, self.x_counter - x, self.y_counter - y)

    def set_counters(self, old_x, old_y, new_x, new_y):
        self.x_counter = self.box.update_x(old_x, new_x)
        self.y_counter = self.box.update_y(old_y, new_y)

    def increase_and_decrease(self):
        if self.box.in_x_interval(self.x_counter):
            if max(self.box.get_x_range()) == self.x_counter:
                self.state = 'decreasing'
            elif min(self.box.get_x_range()) == self.x_counter:
                self.state = 'increasing'
        self.increase() if self.state == 'increasing' else self.decrease()

    def rising_storm(self):
        self.increase(10, 3) if rand(1, 1) < 0.7 else self.decrease(10, 3)

    def calm_water(self):
       self.decrease(4, 10) if rand(1, 1) < 0.7 else self.increase(10, 5)
