from evaluator import Evaluator


class Matcher:

    MATCH_LENGTH = 'length'

    def __init__(self, token_eval):
        self._token_eval = token_eval

    def match(self, text):

        token = self._token_eval[Evaluator.EVAL_TOKEN]
        condition = self._token_eval[Evaluator.EVAL_CONDITION]
        modifier = self._token_eval[Evaluator.EVAL_MODIFIER]

        if condition == Evaluator.EVAL_CONDITION_MATCH:
            cnt = 0
            token_len = len(token)
            while token_len <= len(text) and token == text[0:token_len]:
                cnt = cnt + 1
                text = text[token_len:]

            result = self._modify_result_by_modifier(cnt, modifier)
            return {Matcher.MATCH_LENGTH: result * token_len} if result != None else None

        elif condition == Evaluator.EVAL_CONDITION_ANY:
            cnt = 0
            while cnt < len(text) and text[cnt] in token:
                cnt = cnt + 1

            result = self._modify_result_by_modifier(cnt, modifier)
            return {Matcher.MATCH_LENGTH: result} if result != None else None

        else:
            cnt = 0
            while cnt < len(text) and text[cnt] == token[0]:
                cnt = cnt + 1

            result = self._modify_result_by_modifier(cnt, modifier)
            return {Matcher.MATCH_LENGTH: result} if result != None else None

    def _modify_result_by_modifier(self, result, modifier):
        if modifier == '*':
            return result
        elif modifier == '?':
            return min(result, 1)
        elif modifier == '+':
            return result if result > 0 else None
        else:
            return min(result, 1) if result > 0 else None
