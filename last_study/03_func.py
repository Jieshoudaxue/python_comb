#! /usr/bin/env python3
# -*- coding: utf-8 -*-

########################################

def hello_world():
    print("hello world")
    
new_hello = hello_world

new_hello()

########################################

def ycao_abs(x):
    if x >= 0:
        return x
    else:
        return -x
    
print(ycao_abs(-100))

########################################

def empty_func():
    pass

empty_func()

########################################

def ycao_abs(x):
    if not isinstance(x, (int)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x
    
try:
    print(ycao_abs(-10.0))
except TypeError as e:
    print(e)

########################################

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60)
print(r)
x, y = r
print(f"x: {x}, y: {y}")
########################################

