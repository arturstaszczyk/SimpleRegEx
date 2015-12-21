from unittest import TestCase
from matchers.wildcharmatcher import WildcharMatcher
from evaluator import Evaluator

TOKEN = Evaluator.EVAL_TOKEN
MOD = Evaluator.EVAL_MODIFIER
COND = Evaluator.EVAL_CONDITION
WILD = Evaluator.EVAL_WILDCHAR

class TestWildcharMatcher(TestCase):

    def test_simple_wildchar(self):
        matcher = WildcharMatcher({TOKEN: '.', COND: None, MOD: None, WILD: True})

        output = matcher.match("text");