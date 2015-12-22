from unittest import TestCase

from evaluator import Evaluator
from matchers.regularmatcher import RegularMatcher
from regexexceptions import BadMatcher, NoModifier

TOKEN = Evaluator.EVAL_TOKEN
MOD = Evaluator.EVAL_MODIFIER
COND = Evaluator.EVAL_CONDITION
WILD = Evaluator.EVAL_WILDCHAR

def create_matcher(token_eval):
    return RegularMatcher(token_eval)

class TestMatcher(TestCase):

    def test_no_match(self):
        matcher = create_matcher({TOKEN: 'a', MOD: None, COND: None,
                                  WILD: False})

        result = matcher.get_match_length("text")
        self.assertEquals(result, None)


    # bad data

    def test_no_wildchar(self):
        matcher = create_matcher({TOKEN: 'a', COND: Evaluator.EVAL_CONDITION_ANY, MOD: '*', WILD: True})
        self.assertRaises(BadMatcher, matcher.get_match_length, "text")

    def test_no_modifier(self):
        matcher = create_matcher({TOKEN: 'a', COND: Evaluator.EVAL_CONDITION_MATCH, MOD: None, WILD: False})
        self.assertRaises(NoModifier, matcher.get_match_length, "text")

    # no condition

    def test_no_condition(self):
        matcher = create_matcher({TOKEN: 'a', MOD: None, COND: None,
                                  WILD: False})

        result = matcher.get_match_length("no_artur")
        self.assertEquals(result, None)

        result = matcher.get_match_length("artur")
        self.assertEquals(result, {'length': 1})

        result = matcher.get_match_length("aartur")
        self.assertEquals(result, {'length': 1})

    def test_no_condition_multiple(self):
        matcher = create_matcher({TOKEN: 'a', MOD: '*', COND: None,
                                  WILD: False})

        result = matcher.get_match_length("no_artur")
        self.assertEquals(result, {'length': 0})

        result = matcher.get_match_length("artur")
        self.assertEquals(result, {'length': 1})

        result = matcher.get_match_length("aartur")
        self.assertEquals(result, {'length': 2})

    def test_no_condition_at_least_one(self):
        matcher = create_matcher({TOKEN: 'a', MOD: '+', COND: None,
                                  WILD: False})

        result = matcher.get_match_length("no_artur")
        self.assertEquals(result, None)

        result = matcher.get_match_length("aartur")
        self.assertEquals(result, {'length': 2})

        result = matcher.get_match_length("artur")
        self.assertEquals(result, {'length': 1})

    def test_no_condition_one_or_zero(self):
        matcher = create_matcher({TOKEN: 'a', MOD: '?', COND: None,
                                  WILD: False})

        result = matcher.get_match_length("no_artur")
        self.assertEquals(result, {'length': 0})

        result = matcher.get_match_length("aartur")
        self.assertEquals(result, {'length': 1})

        result = matcher.get_match_length("artur")
        self.assertEquals(result, {'length': 1})

##### condtition 'match' #####

    def test_match_multiple(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: '*', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  WILD: False})

        result = matcher.get_match_length('alibaba')
        self.assertEquals(result, {'length': 0}) # infinite match

        result = matcher.get_match_length('ala')
        self.assertEquals(result, {'length': 3})

        result = matcher.get_match_length('alaal')
        self.assertEquals(result, {'length': 3})

        result = matcher.get_match_length('alabama')
        self.assertEquals(result, {'length': 3})

        result = matcher.get_match_length('alaala')
        self.assertEquals(result, {'length': 6})

    def test_match_at_least_one(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: '+', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  WILD: False})

        result = matcher.get_match_length('alibaba')
        self.assertEquals(result, None)

        result = matcher.get_match_length('ala')
        self.assertEquals(result, {'length': 3})

        result = matcher.get_match_length('alaal')
        self.assertEquals(result, {'length': 3})

        result = matcher.get_match_length('alabama')
        self.assertEquals(result, {'length': 3})

        result = matcher.get_match_length('alaala')
        self.assertEquals(result, {'length': 6})

    def test_match_one_or_zero(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: '?', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  WILD: False})

        result = matcher.get_match_length('alibaba')
        self.assertEquals(result, {'length': 0}) # inifinite

        result = matcher.get_match_length('ala')
        self.assertEquals(result, {'length': 3})

        result = matcher.get_match_length('alaal')
        self.assertEquals(result, {'length': 3})

        result = matcher.get_match_length('alabama')
        self.assertEquals(result, {'length': 3})

        result = matcher.get_match_length('alaala')
        self.assertEquals(result, {'length': 3})

    def test_match_beyond_text(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: '+', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  WILD: False})

        result = matcher.get_match_length("Lal")
        self.assertEquals(result, None)

    def test_match_beyond_text_multiple(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: '*', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  WILD: False})

        result = matcher.get_match_length("Lal")
        self.assertEquals(result, {'length': 0})

    def test_match_beyond_text_at_least_one(self):
        matcher = create_matcher({TOKEN: 'ala', MOD: '+', COND: Evaluator.EVAL_CONDITION_MATCH,
                                  WILD: False})

        result = matcher.get_match_length("Lal")
        self.assertEquals(result, None)

##### condtion 'any' #####

    def test_any_multiple(self):
        matcher = create_matcher({TOKEN: 'liab', MOD: '*', COND: Evaluator.EVAL_CONDITION_ANY,
                                  WILD: False})

        result = matcher.get_match_length('alibaba')
        self.assertEquals(result, {'length': 7})

        result = matcher.get_match_length('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.get_match_length('kot')
        self.assertEquals(result, {'length': 0}) # infinite match

    def test_any_at_least_one(self):
        matcher = create_matcher({TOKEN: 'liab', MOD: '+', COND: Evaluator.EVAL_CONDITION_ANY,
                                  WILD: False})

        result = matcher.get_match_length('alibaba')
        self.assertEquals(result, {'length': 7})

        result = matcher.get_match_length('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.get_match_length('kot')
        self.assertEquals(result, None)

    def test_any_one_or_zero(self):
        matcher = create_matcher({TOKEN: 'liab', MOD: '?', COND: Evaluator.EVAL_CONDITION_ANY,
                                  WILD: False})

        result = matcher.get_match_length('alibaba')
        self.assertEquals(result, {'length': 1})

        result = matcher.get_match_length('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.get_match_length('kot')
        self.assertEquals(result, {'length': 0}) # infinite match

    def test_any(self):
        matcher = create_matcher({TOKEN: 'liab',
                                  MOD: None,
                                  COND: Evaluator.EVAL_CONDITION_ANY,
                                  WILD: False})

        result = matcher.get_match_length('alibaba')
        self.assertEquals(result, {'length': 1})

        result = matcher.get_match_length('lot')
        self.assertEquals(result, {'length': 1})

        result = matcher.get_match_length('kot')
        self.assertEquals(result, None)
