from unittest import TestCase
from matchers.matchercreator import MatcherCreator
from matchers.wildcharmatcher import WildcharMatcher
from matchers.regularmatcher import RegularMatcher


class TestMatcherCreator(TestCase):

    def test_create_wildchar_matcher(self):
        matcher = MatcherCreator.create_matcher({'has_wildchar': True})

        self.assertIsInstance(matcher, WildcharMatcher)

    def test_create_regular_matcher(self):
        matcher = MatcherCreator.create_matcher({'has_wildchar': False})

        self.assertIsInstance(matcher, RegularMatcher)