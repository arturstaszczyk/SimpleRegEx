from tokenizer import Tokenizer
from evaluator import Evaluator
from matcher import Matcher
from matchfinder import MatchFinder


class Engine:

    def __init__(self, tokenizer, evaluator, match_finder):
        self._tokenizer = tokenizer
        self._evaluator = evaluator
        self._match_finder = match_finder

    def find(self, text, regex):

        tokens = self._tokenizer.tokenize(regex)
        evals = self._evaluator.evaluate(tokens)

        matchers = []
        for single_eval in evals:
            matchers.append(Matcher(single_eval))

        self._match_finder.setMatchers(matchers)
        result = self._match_finder.findFirst(text)

        print result
        return text[result[0]:result[1] + 1] if result[1] >= 0 else "Infinite match"

    def findAll(self, text, regex):
        tokens = self._tokenizer.tokenize(regex)
        evals = self._evaluator.evaluate(tokens)

        matchers = []
        for single_eval in evals:
            matchers.append(Matcher(single_eval))

        self._match_finder.setMatchers(matchers)
        scopes = self._match_finder.findAll(text)
        result = []

        print scopes
        for scope in scopes:
            result.append(text[scope[0]:scope[1] + 1])

        return result
