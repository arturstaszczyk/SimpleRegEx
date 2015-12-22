from evaluator import Evaluator
from matcher import Matcher
from regexexceptions import BadCondition, NoModifier, BadMatcher


class WildcharMatcher(Matcher):

    def __init__(self, token_eval):
        self._token_eval = token_eval

    def _raise_exceptions(self, condition, modifier):

        if not self._token_eval[Evaluator.EVAL_WILDCHAR]:
            raise BadMatcher()

        if condition == Evaluator.EVAL_CONDITION_ANY:
            raise BadCondition()

        if condition == Evaluator.EVAL_CONDITION_MATCH and modifier == None:
            raise NoModifier()

    def _match_normal(self, text, token):
        cnt = 0
        while cnt < len(text) and self._chars_wildequal_token(text[cnt], token[0]):
            cnt = cnt + 1

        return cnt

    def _match_any(self, text, token):
        raise NotImplemented("This method should not be called")

    def _match_match(self, text, token):
        cnt = 0
        while cnt < len(text) and self._text_wildequal_token(text, token):
            cnt = cnt + 1
            text = text[len(token):]

        return cnt

    def _chars_wildequal_token(self, char1, token):
        return token == '.'

    def _text_wildequal_token(self, text, token):
        correct_chars = 0
        for char in token:
            if char == '.':
                correct_chars += 1
                continue
            elif char == text[correct_chars]:
                correct_chars += 1
                continue
            else:
                break

        return correct_chars == len(token)


