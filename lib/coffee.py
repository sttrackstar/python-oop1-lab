#!/usr/bin/env python3

class Coffee:
    def __init__(self, name, origin, roast):
        self.name = name
        self.origin = origin
        self.roast = roast

    def __str__(self):
        return f"{self.name} from {self.origin} ({self.roast} roast)"