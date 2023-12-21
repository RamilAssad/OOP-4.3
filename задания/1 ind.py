#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Triad:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def increase(self):
        self.a += 1
        self.b += 1
        self.c += 1

    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"


class Time(Triad):
    def increase(self):
        self.c += 1
        if self.c >= 60:
            self.c = 0
            self.b += 1
            if self.b >= 60:
                self.b = 0
                self.a = (self.a + 1) % 24

    def increase_seconds(self, n):
        self.c += n
        if self.c >= 60:
            self.c -= 60
            self.b += 1
            if self.b >= 60:
                self.b -= 60
                self.a = (self.a + 1) % 24

    def increase_minutes(self, n):
        self.b += n
        if self.b >= 60:
            self.b -= 60
            self.a = (self.a + 1) % 24

    def __str__(self):
        return f"{self.a:02d}:{self.b:02d}:{self.c:02d}"


if __name__ == '__main__':
    triad = Triad(1, 2, 3)
    print("Triad before:", triad)
    triad.increase()
    print("Triad after increase:", triad)

    time = Time(23, 59, 59)
    print("Time before:", time)
    time.increase()
    print("Time after increase:", time)
    time.increase_seconds(120)
    print("Time after 120 seconds increase:", time)
    time.increase_minutes(5)
    print("Time after 5 minutes increase:", time)