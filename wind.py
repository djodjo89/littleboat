#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy.random import rand


class Wind:
    def __init__(self, box):
        self.box = box
        self.x_counter = box.x_min
        self.y_counter = box.y_min
        self.state = 'increasing'
        self.x_strength = 1
        self.y_strength = 1

    def increase(self):
        self.x_counter = self.box.update_x(self.x_counter, self.x_counter + self.x_strength)
        self.y_counter = self.box.update_y(self.y_counter, self.y_counter + 0)

    def decrease(self):
        self.x_counter = self.box.update_x(self.x_counter, self.x_counter - self.x_strength)
        self.y_counter = self.box.update_y(self.y_counter, self.y_counter - 0)

    def increase_and_decrease(self):
        if self.box.in_x_interval(self.x_counter):
            if self.box.x_max == self.x_counter:
                self.state = 'decreasing'
            elif self.box.x_min == self.x_counter:
                self.state = 'increasing'
        self.evolve()

    def evolve(self):
        if self.state == 'increasing':
            self.increase()
        else:
            self.decrease()

    def rising_storm(self):
        U = rand(1, 1)
        if U < 0.7:
            self.increase()
        else:
            self.decrease()
