#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import math

class Array(ABC):
    @abstractmethod
    def addition(self, other):
        pass

    @abstractmethod
    def foreach(self):
        pass

class SortArray(Array):
    def __init__(self, data):
        self.data = sorted(data)

    def addition(self, other):
        return SortArray(list(set(self.data + other.data)))

    def foreach(self):
        return self.data

class XorArray(Array):
    def __init__(self, data):
        self.data = data

    def addition(self, other):
        result = []
        for i in range(len(self.data)):
            result.append(self.data[i] ^ other.data[i])
        return XorArray(result)

    def foreach(self):
        return [math.sqrt(x) for x in self.data]

def print_array(array):
    print(array.foreach())

if __name__ == "__main__":
    arr1 = SortArray([4, 2, 7, 5, 1])
    arr2 = SortArray([5, 7, 3, 8, 1])
    print("Sorted array 1:", arr1.foreach())
    print("Sorted array 2:", arr2.foreach())
    arr3 = arr1.addition(arr2)
    print("Result of addition (SortArray):", arr3.foreach())

    arr4 = XorArray([4, 2, 7, 5, 1])
    arr5 = XorArray([5, 7, 3, 8, 1])
    print("XOR array 1:", arr4.foreach())
    print("XOR array 2:", arr5.foreach())
    arr6 = arr4.addition(arr5)
    print("Result of addition (XorArray):", arr6.foreach())