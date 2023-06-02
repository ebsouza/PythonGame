# -*- coding: utf-8 -*-

import unittest
from domain.generator import SumGenerator, SubGenerator, MultGenerator

from domain.utils import unique_non_zero_random_numbers


class AbstractGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.generator = SumGenerator()
        self.a = 7
        self.b = 14

    def test_generate_question_default_length(self):
        questions = self.generator.generate_question()
        self.assertEqual(len(questions), 10)

    def test_generate_question_defined_length(self):
        questions = self.generator.generate_question(5)
        self.assertEqual(len(questions), 5)

    def test_generate_alternatives_keys(self):
        alternatives = self.generator.generate_alternatives(self.a, self.b)
        alternatives_keys = alternatives.keys()

        self.assertIn("ans", list(alternatives_keys))
        self.assertIn("a", list(alternatives_keys))
        self.assertIn("b", list(alternatives_keys))
        self.assertIn("c", list(alternatives_keys))
        self.assertIn("d", list(alternatives_keys))

    def test_generate_alternatives_values(self):
        alternatives = self.generator.generate_alternatives(self.a, self.b)
        alternatives_values_set = set(alternatives.values())

        alternatives_keys = alternatives.keys()

        self.assertEqual(len(alternatives_values_set), len(alternatives_keys) - 1)


class SumGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.generator = SumGenerator()
        self.a = 5
        self.b = 5

    def test_text(self):
        text = self.generator.text(self.a, self.b)
        self.assertEqual(text, f"{self.a} + {self.b}")

    def test_operate(self):
        result = self.generator.operate(self.a, self.b)
        self.assertEqual(result, self.a + self.b)

    def test_generate_a_b(self):
        a, b = self.generator.generate_a_b()
        self.assertTrue(10 <= a <= 20)
        self.assertTrue(10 <= b <= 20)


class SubGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.generator = SubGenerator()
        self.a = 5
        self.b = 5

    def test_text(self):
        text = self.generator.text(self.a, self.b)
        self.assertEqual(text, f"{self.a} - {self.b}")

    def test_operate(self):
        result = self.generator.operate(self.a, self.b)
        self.assertEqual(result, self.a - self.b)

    def test_generate_a_b(self):
        a, b = self.generator.generate_a_b()
        self.assertTrue(a >= b)
        self.assertTrue(15 <= a <= 30)
        self.assertTrue(10 <= b <= 20)


class MultGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.generator = MultGenerator()
        self.a = 5
        self.b = 5

    def test_text(self):
        text = self.generator.text(self.a, self.b)
        self.assertEqual(text, f"{self.a} * {self.b}")

    def test_operate(self):
        result = self.generator.operate(self.a, self.b)
        self.assertEqual(result, self.a * self.b)

    def test_generate_a_b(self):
        a, b = self.generator.generate_a_b()
        self.assertTrue(a <= b)
        self.assertTrue(5 <= a <= 10)
        self.assertTrue(5 <= b <= 10)


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
