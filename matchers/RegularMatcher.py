from evaluator import Evaluator
from matcher import Matcher
from regexexceptions import BadMatcher, NoModifier


class RegularMatcher(Matcher):

    def __init__(self, token_eval):
        self._token_eval = token_eval

    def _raise_exceptions(self, condition, modifier):
        if self._token_eval[Evaluator.EVAL_WILDCHAR]:
            raise BadMatcher()

        if condition == Evaluator.EVAL_CONDITION_MATCH and modifier == None:
            raise NoModifier()

    def _match_normal(self, text, token):
        cnt = 0
        while cnt < len(text) and text[cnt] == token[0]:
            cnt = cnt + 1

        return cnt

    def _match_any(self, text, token):
        cnt = 0
        while cnt < len(text) and text[cnt] in token:
            cnt = cnt + 1

        return cnt

    def _match_match(self, text, token):
        cnt = 0
        token_len = len(token)
        while token_len <= len(text) and token == text[0:token_len]:
            cnt = cnt + 1
            text = text[token_len:]

        return cnt