from matchers.matchercreator import MatcherCreator


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
            matchers.append(MatcherCreator.create_matcher(single_eval))

        self._match_finder.setMatchers(matchers)
        result = self._match_finder.findFirst(text)

        ret_val = None
        if result:
            print result
            ret_val = text[result[0]:result[1] + 1] if result[1] >= 0 else "Infinite match"
        else:
            ret_val = "No match"

        return ret_val

    def findAll(self, text, regex):
        tokens = self._tokenizer.tokenize(regex)
        evals = self._evaluator.evaluate(tokens)

        matchers = []
        for single_eval in evals:
            matchers.append(MatcherCreator.create_matcher(single_eval))

        self._match_finder.setMatchers(matchers)
        scopes = self._match_finder.findAll(text)
        result = []

        if len(scopes) > 0:
            print scopes
            for scope in scopes:
                result.append(text[scope[0]:scope[1] + 1])

        return result
