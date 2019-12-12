#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy.random import rand


class Wind:
    def __init__(self):
        self.x_counter = 0
        self.y_counter = 0
        self.state = 'increasing'

    def increase(self, x, y):
        self.x_counter += x
        self.y_counter += y

    def decrease(self, x, y):
        self.x_counter -= x
        self.y_counter -= y

    def increase_and_decrease(self):
        if 'increasing' == self.state:
            if 30 > self.x_counter:
                self.increase()
            elif 30 == self.x_counter:
                self.state = 'decreasing'
        else:
            if 1 < self.x_counter:
                self.decrease()
            elif 1 == self.x_counter:
                self.state = 'increasing'

    def rising_storm(self):
        u = rand(1, 1)
        print(u)
        if u < 0.6:
            print('inc')
            self.increase(1, 0)
        else:
            print('dec')
            self.decrease(1, 0)

    def calm_water(self):
        u = rand(1, 1)
        print(u)
        if u < 0.7:
            print('dec')
            self.decrease(0, 1)
            u = rand(1, 1)
            if u < 0.5:
                self.increase(0, 1)
        else:
            print('inc')
            self.increase(0, 1)