#!/usr/bin/env python3

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            print("title must be a string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self._author = value
        else:
            print("author must be a string")

    def read(self):
        print(f"Reading '{self.title}' by {self.author}...")