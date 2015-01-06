#!/usr/bin/env python


__author__ = "bt3"

 ''' understanding generators'''

def fib_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


if __name__ == '__main__':
    fib = fib_generator()
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))