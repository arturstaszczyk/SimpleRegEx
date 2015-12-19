from unittest import TestCase
from evaluator import Evaluator


class TestEvaluator(TestCase):

    def setUp(self):
        self._evaluator = Evaluator()

    def test_evaluate_simple_tokens(self):
        tokens = ['a'] * 3
        expected = [{'token': 'a', 'modifier': None, 'condition': None}] * 3

        output = evaluation = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_simple_tokens_modifier1(self):
        tokens = ['a+']
        expected = [{'token': 'a', 'modifier': '+', 'condition': None}]

        output = evaluation = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_simple_tokens_modifier2(self):
        tokens = ['a*']
        expected = [{'token': 'a', 'modifier': '*', 'condition': None}]

        output = evaluation = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_advanced_tokens_modifier1(self):
        tokens = ['[ab]+']
        expected = [{'token': 'ab', 'modifier': '+', 'condition': 'any'}]

        output = evaluation = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_advanced_tokens_modifier2(self):
        tokens = ['(ab)+']
        expected = [{'token': 'ab', 'modifier': '+', 'condition': 'match'}]

        output = evaluation = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_advanced_tokens_modifier3(self):
        tokens = ['(ab)']
        expected = [{'token': 'ab', 'modifier': None, 'condition': 'match'}]

        output = evaluation = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)