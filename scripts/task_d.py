#!/usr/bin/env python
import timeit
import random


def case_d():
    counter = 0
    long_list_to_sort = []
    start = timeit.default_timer()
    while counter < 10000:
        a = random.randint(100, 10000)
        b = random.randint(100, 10000)
        python_has_powers = a ** b
        long_list_to_sort.append(python_has_powers)
        counter = counter + 1
        # print(a,b)
    stop = timeit.default_timer()
    # print(sorted(long_list_to_sort))
    print("--- %s seconds ---" % (stop - start))


def main():
    case_d()


if __name__ == '__main__':
    main()
