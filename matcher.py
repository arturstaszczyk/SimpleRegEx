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

        if modifier == None:
            if condition == None:
                if text[0] == self._current_char:
                    return {Matcher.MATCH_LENGTH: 1}

            if condition == Evaluator.EVAL_CONDITION_ANY:
                if text[0] in token:
                    return {Matcher.MATCH_LENGTH: 1}


        elif modifier == '*':
            if condition == None:
                cnt = 0;
                while cnt < len(text) and text[cnt] == self._current_char:
                    cnt = cnt + 1

                return {Matcher.MATCH_LENGTH: cnt}

            elif condition == Evaluator.EVAL_CONDITION_MATCH:
                cnt = 0
                token_len = len(token)
                while token_len <= len(text) and token == text[0:token_len]:
                    cnt = cnt + 1
                    text = text[token_len:]

                return {Matcher.MATCH_LENGTH: cnt*token_len}
            else:
                cnt = 0
                while cnt < len(text) and text[cnt] in token:
                    cnt = cnt + 1

                return {Matcher.MATCH_LENGTH: cnt}

        elif modifier == '+':
            if condition == None:
                cnt = 0
                while cnt < len(text) and text[cnt] == token[0]:
                    cnt = cnt + 1

                return {Matcher.MATCH_LENGTH: cnt} if cnt > 0 else None

            elif condition == Evaluator.EVAL_CONDITION_MATCH:
                cnt = 0
                token_len = len(token)
                while token_len <= len(text) and token == text[0:token_len]:
                    cnt = cnt + 1
                    text = text[token_len:]

                return {Matcher.MATCH_LENGTH: cnt*token_len} if cnt > 0 else None
            else:
                cnt = 0
                while cnt < len(text) and text[cnt] in token:
                    cnt = cnt + 1

                return {Matcher.MATCH_LENGTH: cnt} if cnt > 0 else None

        elif modifier == '?':
            if condition == Evaluator.EVAL_CONDITION_ANY:
                if text[0] in token:
                    return {Matcher.MATCH_LENGTH: 1}
                else:
                    return {Matcher.MATCH_LENGTH: 0}

            elif condition in [Evaluator.EVAL_CONDITION_MATCH, None]:
                token_len = len(token)
                if token_len <= len(text) and token == text[0:token_len]:
                    return {Matcher.MATCH_LENGTH: token_len}

                return {Matcher.MATCH_LENGTH: 0}


        return None
