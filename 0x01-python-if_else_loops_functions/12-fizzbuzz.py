#!/usr/bin/python3
def fizzbuzz():
    for i in range(1:100):
        if i == i % 3:
            print("Fizz")
        elif i == i % 5:
            print("Buzz")
        elif i == i % 3 and i == i % 5:
            print("FizzBuzz")
        else:
            print({":d"}.format(i), end="")
