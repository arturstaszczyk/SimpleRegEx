from unittest import TestCase
from matchers.wildcharmatcher import WildcharMatcher
from evaluator import Evaluator
from regexexceptions import BadCondition, BadMatcher, NoModifier

TOKEN = Evaluator.EVAL_TOKEN
MOD = Evaluator.EVAL_MODIFIER
COND = Evaluator.EVAL_CONDITION
WILD = Evaluator.EVAL_WILDCHAR

class TestWildcharMatcher(TestCase):

# bad data

    def test_no_wildchar(self):
        matcher = WildcharMatcher({TOKEN: '.a', COND: Evaluator.EVAL_CONDITION_ANY, MOD: '*', WILD: False})
        self.assertRaises(BadMatcher, matcher.match, "text")

    def test_bad_wildcahr_condition(self):
        matcher = WildcharMatcher({TOKEN: '.a', COND: Evaluator.EVAL_CONDITION_ANY, MOD: '*', WILD: True})
        self.assertRaises(BadCondition, matcher.match, "text")

    def test_no_modifier(self):
        matcher = WildcharMatcher({TOKEN: '.a', COND: Evaluator.EVAL_CONDITION_MATCH, MOD: None, WILD: True})
        self.assertRaises(NoModifier, matcher.match, "text")

# condition = None

    def test_wildchar(self):
        matcher = WildcharMatcher({TOKEN: '.', COND: None, MOD: None, WILD: True})

        output = matcher.match("text")
        self.assertEquals(output, {"length": 1})

    def test_wildchar_multiply(self):
        matcher = WildcharMatcher({TOKEN: '.', COND: None, MOD: '*', WILD: True})

        output = matcher.match("text")
        self.assertEquals(output, {"length": 4})

    def test_wildchar_one_or_more(self):
        matcher = WildcharMatcher({TOKEN: '.', COND: None, MOD: '+', WILD: True})

        output = matcher.match("text")
        self.assertEquals(output, {"length": 4})

    def test_wildchar_one_or_zero(self):
        matcher = WildcharMatcher({TOKEN: '.', COND: None, MOD: '?', WILD: True})

        output = matcher.match("text")
        self.assertEquals(output, {"length": 1})

# condition = Matxh

    def test_wildchar_match_multiply(self):
        matcher = WildcharMatcher({TOKEN: '.a', COND: Evaluator.EVAL_CONDITION_MATCH, MOD: '*', WILD: True})

        output = matcher.match("taken")
        self.assertEquals(output, {"length": 2})

    def test_wildchar_match_more_than_one(self):
        matcher = WildcharMatcher({TOKEN: '.a', COND: Evaluator.EVAL_CONDITION_MATCH, MOD: '+', WILD: True})

        output = matcher.match("tabaco")
        self.assertEquals(output, {"length": 4})

    def test_wildchar_match_one_or_zero(self):
        matcher = WildcharMatcher({TOKEN: '.a', COND: Evaluator.EVAL_CONDITION_MATCH, MOD: '?', WILD: True})

        output = matcher.match("tabaco")
        self.assertEquals(output, {"length": 2})

    #special cases

    def test_special_case1(self):
        matcher = WildcharMatcher({TOKEN: 'a.', COND: Evaluator.EVAL_CONDITION_MATCH, MOD: '+', WILD: True})

        output = matcher.match("alabama")
        self.assertEquals(output, {"length": 6})