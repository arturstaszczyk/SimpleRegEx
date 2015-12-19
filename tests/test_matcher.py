from unittest import TestCase
from matcher import Matcher
from evaluator import Evaluator

TOKEN = Evaluator.EVAL_TOKEN
MOD = Evaluator.EVAL_MODIFIER
COND = Evaluator.EVAL_CONDITION

class TestMatcher(TestCase):

    def test_no_match(self):
        matcher = Matcher({TOKEN: 'a', MOD: None, COND: None})

        result = matcher.match("text")
        self.assertEquals(result, None)

##### no condition #####

    def test_no_condition(self):
        matcher = Matcher({TOKEN: 'a', MOD: None, COND: None})

        result = matcher.match("no_artur")
        self.assertEquals(result, None)

        result = matcher.match("artur")
        self.assertEquals(result, {'length': 1})

        result = matcher.match("aartur")
        self.assertEquals(result, {'length': 1})

    def test_no_condition_multiple(self):
        matcher = Matcher({TOKEN: 'a', MOD: '*', COND: None})

        result = matcher.match("no_artur")
        self.assertEquals(result, {'length': 0})

        result = matcher.match("artur")
        self.assertEquals(result, {'length': 1})

        result = matcher.match("aartur")
        self.assertEquals(result, {'length': 2})

    def test_no_condition_at_least_one(self):
        matcher = Matcher({TOKEN: 'a', MOD: '+', COND: None})

        result = matcher.match("no_artur")
        self.assertEquals(result, None)

        result = matcher.match("aartur")
        self.assertEquals(result, {'length': 2})

        result = matcher.match("artur")
        self.assertEquals(result, {'length': 1})

    def test_no_condition_one_or_zero(self):
        matcher = Matcher({TOKEN: 'a', MOD: '?', COND: None})

        result = matcher.match("no_artur")
        self.assertEquals(result, {'length': 0})

        result = matcher.match("aartur")
        self.assertEquals(result, {'length': 1})

        result = matcher.match("artur")
        self.assertEquals(result, {'length': 1})

##### condtition 'match' #####

    def test_match_multiple(self):
        matcher = Matcher({TOKEN: 'ala', MOD: '*', COND: Evaluator.EVAL_CONDITION_MATCH})

        result = matcher.match('alibaba')
        self.assertEquals(result, {'length': 0}) # infinite match

        result = matcher.match('ala')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alaal')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alabama')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alaala')
        self.assertEquals(result, {'length': 6})

    def test_match_at_least_one(self):
        matcher = Matcher({TOKEN: 'ala', MOD: '+', COND: Evaluator.EVAL_CONDITION_MATCH})

        result = matcher.match('alibaba')
        self.assertEquals(result, None)

        result = matcher.match('ala')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alaal')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alabama')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alaala')
        self.assertEquals(result, {'length': 6})

    def test_match_one_or_zero(self):
        matcher = Matcher({TOKEN: 'ala', MOD: '?', COND: Evaluator.EVAL_CONDITION_MATCH})

        result = matcher.match('alibaba')
        self.assertEquals(result, {'length': 0}) # inifinite

        result = matcher.match('ala')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alaal')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alabama')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alaala')
        self.assertEquals(result, {'length': 3})

##### condtion 'any' #####

    def test_any_multiple(self):
        matcher = Matcher({TOKEN: 'liab', MOD: '*', COND: Evaluator.EVAL_CONDITION_ANY})

        result = matcher.match('alibaba')
        self.assertEquals(result, {'length': 7})

        result = matcher.match('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.match('kot')
        self.assertEquals(result, {'length': 0}) # infinite match

    def test_any_at_least_one(self):
        matcher = Matcher({TOKEN: 'liab', MOD: '+', COND: Evaluator.EVAL_CONDITION_ANY})

        result = matcher.match('alibaba')
        self.assertEquals(result, {'length': 7})

        result = matcher.match('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.match('kot')
        self.assertEquals(result, None)

    def test_any_one_or_zero(self):
        matcher = Matcher({TOKEN: 'liab', MOD: '?', COND: Evaluator.EVAL_CONDITION_ANY})

        result = matcher.match('alibaba')
        self.assertEquals(result, {'length': 1})

        result = matcher.match('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.match('kot')
        self.assertEquals(result, {'length': 0}) # infinite match