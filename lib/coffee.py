#!/usr/bin/env python3

class Coffee:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if isinstance(value, int):
            self._strength = value
        else:
            print("strength must be an integer")

    def brew(self):
        print(f"Brewing a cup of {self.name} with strength {self.strength}...")