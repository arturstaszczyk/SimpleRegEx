from evaluator import Evaluator
from matchers.wildcharmatcher import WildcharMatcher
from matchers.regularmatcher import RegularMatcher


class MatcherCreator:

    @staticmethod
    def create_matcher(token_eval):
        if token_eval[Evaluator.EVAL_WILDCHAR]:
            return WildcharMatcher(token_eval)
        else:
            return RegularMatcher(token_eval)
