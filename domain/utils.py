# -*- coding: utf-8 -*-

import random


def unique_non_zero_random_numbers(n=1, min=-5, max=5):

    numbers = set()

    while len(numbers) < n:
        element = random.randint(min, max)

        if element == 0:
            continue

        numbers.add(element)

    return list(numbers)
