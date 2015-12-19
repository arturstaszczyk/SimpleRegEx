from evaluator import Evaluator


class Matcher:

    MATCH_LENGTH = 'length'

    def __init__(self, token_eval):
        self._token_eval = token_eval
        self._current_char = token_eval[Evaluator.EVAL_TOKEN]

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

            if modifier == '*':
                return {Matcher.MATCH_LENGTH: cnt * token_len}
            elif modifier == '?':
                return {Matcher.MATCH_LENGTH: min(cnt, 1) * token_len}
            elif modifier == '+':
                return {Matcher.MATCH_LENGTH: cnt * token_len} if cnt > 0 else None
            else:
                return {Matcher.MATCH_LENGTH: min(cnt, 1) * token_len} if cnt > 0 else None

        elif condition == Evaluator.EVAL_CONDITION_ANY:
            cnt = 0
            while cnt < len(text) and text[cnt] in token:
                cnt = cnt + 1

            if modifier == '*':
                return {Matcher.MATCH_LENGTH: cnt}
            elif modifier == '?':
                return {Matcher.MATCH_LENGTH: min(cnt, 1)}
            elif modifier == '+':
                return {Matcher.MATCH_LENGTH: cnt} if cnt > 0 else None
            else:
                return {Matcher.MATCH_LENGTH: min(cnt, 1)} if cnt > 0 else None

        else:
            cnt = 0
            while cnt < len(text) and text[cnt] == token[0]:
                cnt = cnt + 1

            if modifier == '*':
                return {Matcher.MATCH_LENGTH: cnt}
            elif modifier == '?':
                return {Matcher.MATCH_LENGTH: min(cnt, 1)}
            elif modifier == '+':
                return {Matcher.MATCH_LENGTH: cnt} if cnt > 0 else None
            else:
                return {Matcher.MATCH_LENGTH: min(cnt, 1)} if cnt > 0 else None
