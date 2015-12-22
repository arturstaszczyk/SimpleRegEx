from unittest import TestCase
from mock import Mock
from matchfinder import MatchFinder

text = 'my awesome text'
text_len = len(text)

class TestMatchFinder(TestCase):

    def setUp(self):
        self._matchFinder = MatchFinder()

    def test_find_first_with_two_matchers_at_begining(self):

        mock_matcher1 = Mock()
        mock_matcher2 = Mock()
        mock_matcher1.get_match_length.side_effect = [{'length': 2}]
        mock_matcher2.get_match_length.side_effect = [{'length': 3}]

        self._matchFinder.setMatchers([mock_matcher1, mock_matcher2])

        result = self._matchFinder.findFirst(text)
        self.assertSequenceEqual(result, [0, 4]) # length = 5 (2+3), index 0 to 4

    def test_find_first_with_two_matchers_no_begining(self):

        mock_matcher1 = Mock()
        mock_matcher2 = Mock()

        mock_matcher1.get_match_length.side_effect = [None, {'length': 2}]
        mock_matcher2.get_match_length.side_effect = [{'length': 3}]

        self._matchFinder.setMatchers([mock_matcher1, mock_matcher2])

        result = self._matchFinder.findFirst(text)
        self.assertSequenceEqual(result, [1, 5])

    def test_find_first_with_two_matchers_fail_on_second(self):
        mock_matcher1 = Mock()
        mock_matcher2 = Mock()

        results1 = [{'length': 2}] + ([None] * 100)
        mock_matcher1.get_match_length.side_effect = results1
        mock_matcher2.get_match_length.side_effect = [None]

        self._matchFinder.setMatchers([mock_matcher1, mock_matcher2])

        result = self._matchFinder.findFirst(text)
        self.assertEquals(result, None)

    def test_find_first_with_two_matchers_end_of_text(self):
        mock_matcher1 = Mock()
        mock_matcher2 = Mock()

        results1 = ([None] * (text_len - 3)) + [{'length': 2}]
        mock_matcher1.get_match_length.side_effect = results1
        mock_matcher2.get_match_length.side_effect = [{'length': 1}]

        self._matchFinder.setMatchers([mock_matcher1, mock_matcher2])

        result = self._matchFinder.findFirst(text)
        self.assertEquals(result, [text_len - 3, text_len-1])

    def test_find_first_with_inifinite_match(self):
        mock_matcher1 = Mock()
        mock_matcher2 = Mock()

        results1 = ([None] * (text_len - 3)) + [{'length': 2}]
        mock_matcher1.get_match_length.side_effect = results1
        mock_matcher2.get_match_length.side_effect = [{'length': 1}]

        self._matchFinder.setMatchers([mock_matcher1, mock_matcher2])

        result = self._matchFinder.findFirst(text)
        self.assertEquals(result, [text_len - 3, text_len-1])

    def test_find_all_two_matchers(self):
        mock_matcher1 = Mock()
        mock_matcher2 = Mock()

        mock_matcher1.get_match_length.side_effect = [{'length': 2}, {'length': 2}] + ([None] * 100)
        mock_matcher2.get_match_length.side_effect = [{'length': 1}, {'length': 1}]

        self._matchFinder.setMatchers([mock_matcher1, mock_matcher2])

        result = self._matchFinder.findAll(text)
        self.assertEquals(result, [[0, 2], [3, 5]])