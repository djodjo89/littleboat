#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy.random import rand


class Wind:
    def __init__(self):
        self.x_counter = 0
        self.y_counter = 0
        self.state = 'increasing'

    def increase(self):
        self.x_counter += 1
        self.y_counter += 0

    def decrease(self):
        self.x_counter -= 1
        self.y_counter -= 0

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
        U = rand(1, 1)
        print(U)
        if U < 0.6:
            print('inc')
            self.increase()
        else:
            print('dec')
            self.decrease()
