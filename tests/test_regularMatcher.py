from unittest import TestCase

from evaluator import Evaluator
from matchers.matcher import Matcher

TOKEN = Evaluator.EVAL_TOKEN
MOD = Evaluator.EVAL_MODIFIER
COND = Evaluator.EVAL_CONDITION

def create_matcher(token_eval):
    return Matcher.create_matcher(token_eval)

class TestMatcher(TestCase):

    def test_no_match(self):
        matcher = create_matcher({TOKEN: 'a', MOD: None, COND: None,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match("text")
        self.assertEquals(result, None)

##### no condition #####

    def test_no_condition(self):
        matcher = create_matcher({TOKEN: 'a', MOD: None, COND: None,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match("no_artur")
        self.assertEquals(result, None)

        result = matcher.match("artur")
        self.assertEquals(result, {'length': 1})

        result = matcher.match("aartur")
        self.assertEquals(result, {'length': 1})

    def test_no_condition_multiple(self):
        matcher = create_matcher({TOKEN: 'a', MOD: '*', COND: None,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match("no_artur")
        self.assertEquals(result, {'length': 0})

        result = matcher.match("artur")
        self.assertEquals(result, {'length': 1})

        result = matcher.match("aartur")
        self.assertEquals(result, {'length': 2})

    def test_no_condition_at_least_one(self):
        matcher = create_matcher({TOKEN: 'a', MOD: '+', COND: None,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match("no_artur")
        self.assertEquals(result, None)

        result = matcher.match("aartur")
        self.assertEquals(result, {'length': 2})

        result = matcher.match("artur")
        self.assertEquals(result, {'length': 1})

    def test_no_condition_one_or_zero(self):
        matcher = create_matcher({TOKEN: 'a', MOD: '?', COND: None,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match("no_artur")
        self.assertEquals(result, {'length': 0})

        result = matcher.match("aartur")
        self.assertEquals(result, {'length': 1})

        result = matcher.match("artur")
        self.assertEquals(result, {'length': 1})

##### condtition 'match' #####

    def test_match_multiple(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: '*', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  Evaluator.EVAL_WILDCHAR: False})

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
        matcher = create_matcher({TOKEN: 'ala', MOD: '+', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  Evaluator.EVAL_WILDCHAR: False})

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
        matcher = create_matcher({TOKEN: 'ala', MOD: '?', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  Evaluator.EVAL_WILDCHAR: False})

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

    def test_match(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: None, COND: Evaluator.EVAL_CONDITION_MATCH,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match('alibaba')
        self.assertEquals(result, None)

        result = matcher.match('ala')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alaal')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alabama')
        self.assertEquals(result, {'length': 3})

        result = matcher.match('alaala')
        self.assertEquals(result, {'length': 3})

    def test_match_beyond_text(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: None, COND: Evaluator.EVAL_CONDITION_MATCH,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match("Lal")
        self.assertEquals(result, None)

    def test_match_beyond_text_multiple(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: '*', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match("Lal")
        self.assertEquals(result, {'length': 0})

    def test_match_beyond_text_at_least_one(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: '+', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match("Lal")
        self.assertEquals(result, None)

##### condtion 'any' #####

    def test_any_multiple(self):
        matcher = create_matcher({TOKEN: 'liab', MOD: '*', COND: Evaluator.EVAL_CONDITION_ANY,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match('alibaba')
        self.assertEquals(result, {'length': 7})

        result = matcher.match('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.match('kot')
        self.assertEquals(result, {'length': 0}) # infinite match

    def test_any_at_least_one(self):
        matcher = create_matcher({TOKEN: 'liab', MOD: '+', COND: Evaluator.EVAL_CONDITION_ANY,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match('alibaba')
        self.assertEquals(result, {'length': 7})

        result = matcher.match('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.match('kot')
        self.assertEquals(result, None)

    def test_any_one_or_zero(self):
        matcher = create_matcher({TOKEN: 'liab', MOD: '?', COND: Evaluator.EVAL_CONDITION_ANY,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match('alibaba')
        self.assertEquals(result, {'length': 1})

        result = matcher.match('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.match('kot')
        self.assertEquals(result, {'length': 0}) # infinite match

    def test_any(self):
        matcher = create_matcher({TOKEN: 'liab',
                                  MOD: None,
                                  COND: Evaluator.EVAL_CONDITION_ANY,
                                  Evaluator.EVAL_WILDCHAR: False})

        result = matcher.match('alibaba')
        self.assertEquals(result, {'length': 1})

        result = matcher.match('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.match('kot')
        self.assertEquals(result, None)
