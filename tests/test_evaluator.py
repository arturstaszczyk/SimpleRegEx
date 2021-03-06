from unittest import TestCase
from evaluator import Evaluator


class TestEvaluator(TestCase):

    def setUp(self):
        self._evaluator = Evaluator()

    def test_evaluate_simple_tokens(self):
        tokens = ['a'] * 3
        expected = [{'token': 'a', 'modifier': None, 'condition': None, 'has_wildchar': False}] * 3

        output = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_simple_tokens_modifier1(self):
        tokens = ['a+']
        expected = [{'token': 'a', 'modifier': '+', 'condition': None, 'has_wildchar': False}]

        output = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_simple_tokens_modifier2(self):
        tokens = ['a*']
        expected = [{'token': 'a', 'modifier': '*', 'condition': None, 'has_wildchar': False}]

        output = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_advanced_tokens_modifier1(self):
        tokens = ['[ab]+']
        expected = [{'token': 'ab', 'modifier': '+', 'condition': 'any', 'has_wildchar': False}]

        output = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_advanced_tokens_modifier2(self):
        tokens = ['(ab)+']
        expected = [{'token': 'ab', 'modifier': '+', 'condition': 'match', 'has_wildchar': False}]

        output = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_advanced_tokens_modifier3(self):
        tokens = ['(ab)']
        expected = [{'token': 'ab', 'modifier': None, 'condition': 'match', 'has_wildchar': False}]

        output = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_wildchar_token(self):
        tokens = ['.']
        expected = [{'token': '.', 'modifier': None, 'condition': None, 'has_wildchar': True}]

        output = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)

    def test_evaluate_wildchar_any_token(self):
        tokens = ['[.a]+'] # in this case . should be evaluated as '.'
        expected = [{'token': '.a', 'modifier': '+',
                     'condition': Evaluator.EVAL_CONDITION_ANY, 'has_wildchar': False}]

        output = self._evaluator.evaluate(tokens)
        self.assertSequenceEqual(output, expected)