from unittest import TestCase

from mock import patch, call, Mock
from matcher import Matcher
from matchfinder import MatchFinder

text = 'my awesome text'
text_len = len(text)

class TestMatchFinder(TestCase):

    def setUp(self):
        self._matchFinder = MatchFinder()

    def test_find_first_with_two_matchers_at_begining(self):

        mock_matcher1 = Mock();
        mock_matcher2 = Mock();
        mock_matcher1.match.side_effect = [{Matcher.MATCH_LENGTH: 2}]
        mock_matcher2.match.side_effect = [{Matcher.MATCH_LENGTH: 3}]

        self._matchFinder.setMatchers([mock_matcher1, mock_matcher2])

        result = self._matchFinder.findFirst(text)
        self.assertSequenceEqual(result, [0, 5])

    def test_find_first_with_two_matchers_no_begining(self):

        mock_matcher1 = Mock();
        mock_matcher2 = Mock();

        mock_matcher1.match.side_effect = [None, {Matcher.MATCH_LENGTH: 2}]
        mock_matcher2.match.side_effect = [{Matcher.MATCH_LENGTH: 3}]

        self._matchFinder.setMatchers([mock_matcher1, mock_matcher2])

        result = self._matchFinder.findFirst(text)
        self.assertSequenceEqual(result, [1, 6])
