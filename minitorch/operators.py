"""Collection of the core mathematical operators used throughout the code base."""

import math
import builtins

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(a, b):
    return a * b

def id(a):
    return a

def add(a, b):
    return a + b

def neg(a):
    return float(-a)

def lt(a, b):
    return a < b

def eq(a, b):
    return a == b

def max(a, b):
    return builtins.max(a, b)

def is_close(a, b):
    return abs(a - b) < 1e2

def sigmoid(a):
    return 1 / (1 + math.exp(-a)) if a >= 0 else (math.exp(a)) / (1 + math.exp(a))

def relu(a):
    return max(0.0, a)

def log(a):
    return float(math.log(a))

def exp(a):
    return float(math.exp(a))

def inv(a):
    return 1.0 / a

def log_back(a, b):
    return b / a

def inv_back(a, b):
    return - b / (a * a)

def relu_back(a, b):
    return b if a >= 0 else  0.0

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(f: Callable, l: Iterable):
   return iter(f(i) for i in l)

def zipWith(f: Callable, list1: Iterable, list2: Iterable):
    return iter(f(a, b) for a, b in zip(list1, list2))

def reduce(f:Callable, l: Iterable):
    it = iter(l)
    a = next(it)
    for i in it:
        a = f(a, i)
    return a

def negList(l: list):
    return map(neg, l)

def sum(l: list):
    if not l:
        return 0.0
    return reduce(add, l)

def addLists(l1:list, l2:list):
    return zipWith(add, l1, l2)

def prod(l:list):
    return reduce(mul, l)

