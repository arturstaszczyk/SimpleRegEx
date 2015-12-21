from unittest import TestCase
from tokenizer import Tokenizer


class TestTokenizer(TestCase):

    def setUp(self):
        self._tokenizer = Tokenizer()

    def tearDown(self):
        self._tokenizer = None

    def test_tokenize_simple(self):
        tokens = self._tokenizer.tokenize("aaa")
        self.assertSequenceEqual(tokens, ['a', 'a', 'a'])

    def test_tokenize_special_char(self):
        tokens = self._tokenizer.tokenize("aa+")
        self.assertSequenceEqual(tokens, ['a', 'a+'])

    def test_tokenize_multiple_special_char(self):
        tokens = self._tokenizer.tokenize('aa+bb*[wf]+(ss)?')
        self.assertSequenceEqual(tokens, ['a', 'a+', 'b', 'b*', '[wf]+', '(ss)?'])

    def test_tokenize_awesome_case_1(self):
        tokens = self._tokenizer.tokenize(".?[ab]+")
        self.assertSequenceEqual(tokens, ['.?', '[ab]+'])

    def test_tokenize_awesome_case_2(self):
        tokens = self._tokenizer.tokenize(".?[ab]+a")
        self.assertSequenceEqual(tokens, ['.?', '[ab]+', 'a'])

    def test_tokenize_awesome_case_3(self):
        tokens = self._tokenizer.tokenize(".?[ab]a")
        self.assertSequenceEqual(tokens, ['.?', '[ab]', 'a'])

    def test_tokenize_awesome_case_4(self):
        tokens = self._tokenizer.tokenize(".?[ab]a")
        self.assertSequenceEqual(tokens, ['.?', '[ab]', 'a'])

    def test_tokenize_awesome_case_5(self):
        tokens = self._tokenizer.tokenize(".?(ab)[AB]a")
        self.assertSequenceEqual(tokens, ['.?', '(ab)', '[AB]', 'a'])

    def test_tokenize_wildchar(self):
        tokens = self._tokenizer.tokenize(".?(.a)+[ba]*.")
        self.assertSequenceEqual(tokens, ['.?', '(.a)+', '[ba]*', '.'])