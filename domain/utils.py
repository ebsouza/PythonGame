# -*- coding: utf-8 -*-

import random


def unique_non_zero_random_numbers(length=0, min_max=(-100, 100)):

    if not length:
        return list()

    random_numbers = list()
    tmp = random.randint(min_max[0], min_max[1])

    for i in range(length):

        while tmp in random_numbers or tmp == 0:
            tmp = random.randint(min_max[0], min_max[1])

        random_numbers.append(tmp)

    return random_numbers
