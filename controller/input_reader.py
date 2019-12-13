#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class InputReader:
    # For testing purposes only
    def ask_parameter(self, param, range):
        try:
            param_sail = int(input("Saisissez " + param + " (compris entre {} et {}): ".format(min(range), max(range))))
            if param_sail not in range:
                return self.ask_parameter(param, range)
            else:
                return param_sail
        except ValueError:
            print("Veuillez saisir un entier")
            return self.ask_parameter(param, range)
