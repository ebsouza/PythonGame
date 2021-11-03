# -*- coding: utf-8 -*-

import unittest
from modules.question import SumGenerator, SubGenerator, MultGenerator
from modules.utils import unique_non_zero_random_numbers


class SumGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.generator = SumGenerator()

    def test_question_length(self):
        questions = self.generator.generate_question()
        self.assertEqual(len(questions), 10)


class SubGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.generator = SubGenerator()

    def test_question_length(self):
        questions = self.generator.generate_question()
        self.assertEqual(len(questions), 10)


class MultGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.generator = MultGenerator()

    def test_question_length(self):
        questions = self.generator.generate_question()
        self.assertEqual(len(questions), 10)


class UtilsTest(unittest.TestCase):

    def test_unique_non_zero_random_numbers_length(self):
        numbers_list = unique_non_zero_random_numbers(10)
        numbers_set = set(numbers_list)
        self.assertTrue(isinstance(numbers_list, list))
        self.assertEqual(len(numbers_list), len(numbers_set))

    def test_unique_non_zero_random_numbers_range(self):
        min_value, max_value = -20, 20
        numbers_list = unique_non_zero_random_numbers(10, (min_value, max_value))
        self.assertTrue(min(numbers_list) >= min_value)
        self.assertTrue(max(numbers_list) <= max_value)


if __name__ == '__main__':
    unittest.main()
