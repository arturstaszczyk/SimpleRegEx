from abc import ABCMeta, abstractmethod
from evaluator import Evaluator


class Matcher:

    __metaclass__ = ABCMeta

    KEY_MATCH_LENGTH = 'length'

    def __init__(self, token_eval):
        self._token_eval = token_eval

    def get_match_length(self, text):
        token = self._token_eval[Evaluator.EVAL_TOKEN]
        condition = self._token_eval[Evaluator.EVAL_CONDITION]
        modifier = self._token_eval[Evaluator.EVAL_MODIFIER]

        self._raise_exceptions(condition, modifier)

        if condition == None:
            result = self._match_normal(text, token)
            result = self._modify_result_by_modifier(result, modifier)

        elif condition == Evaluator.EVAL_CONDITION_MATCH:
            result = self._match_match(text, token)
            result = self._modify_result_by_modifier(result, modifier)
            result = result * len(token) if result is not None else result

        elif condition == Evaluator.EVAL_CONDITION_ANY:
            result = self._match_any(text, token)
            result = self._modify_result_by_modifier(result, modifier)

        return {Matcher.KEY_MATCH_LENGTH: result} if result != None else None


    def _modify_result_by_modifier(self, result, modifier):
        if modifier == '*':
            return result
        elif modifier == '?':
            return min(result, 1)
        elif modifier == '+':
            return result if result > 0 else None
        else:
            return min(result, 1) if result > 0 else None

    @abstractmethod
    def _raise_exceptions(self, condition, modifier):
        pass

    @abstractmethod
    def _match_normal(self, text, token):
        pass

    @abstractmethod
    def _match_any(self, text, token):
        pass

    @abstractmethod
    def _match_match(self, text, token):
        pass