#!/usr/bin/env python

# C) Write a function that sorts 11 small numbers (<100) as fast as possible.
# Estimate how long it would take to execute that function 10 Billion (10^10) times on a normal machine?

import timeit
import random


def case_c1():
    start = timeit.default_timer()
    x = random.sample(range(0, 100), 11)
    y = sorted(x)
    stop = timeit.default_timer()
    print('random numbers: ' + str(x))
    print('sorted numbers: ' + str(y))
    print("--- %s seconds ---" % (stop - start))


def case_c2():
    start = timeit.default_timer()
    x = random.sample(range(0, 100), 11)
    print('random numbers: ' + str(x))
    x.sort()
    stop = timeit.default_timer()
    print('sorted numbers: ' + str(x))
    print("--- %s seconds ---" % (stop - start))


def case_c3():
    timeit.timeit('import random; sorted(random.sample(range(0, 100), 11))', number=100)


def main():
    case_c1()


if __name__ == '__main__':
    main()
