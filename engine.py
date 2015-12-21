from tokenizer import Tokenizer
from evaluator import Evaluator
from matcher import Matcher
from matchfinder import MatchFinder


class Engine:

    def find(self, text, regex):
        tokenizer = Tokenizer()
        evaluator = Evaluator();

        tokens = tokenizer.tokenize(regex)
        evals = evaluator.evaluate(tokens)
        matchers = []

        for single_eval in evals:
            matchers.append(Matcher(single_eval))

        match_finder = MatchFinder()
        match_finder.setMatchers(matchers)
        result = match_finder.findFirst(text)

        print result
        return text[result[0]:result[1] + 1] if result[1] >= 0 else "Infinite match"


