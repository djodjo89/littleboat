#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class InputReader:
    # For testing purposes only
    def ask_parameter(self, param, min, max):
        try:
            param_sail = int(input("Saisissez " + param + " (compris entre {} et {}): ".format(min, max)))
            if param_sail < min or param_sail > max:
                self.ask_parameter(param, min, max)
            return param_sail
        except ValueError:
            print("Veuillez saisir un entier")
            return self.ask_parameter(param, min, max)
