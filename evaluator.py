class Evaluator:

    EVAL_TOKEN = 'token'
    EVAL_MODIFIER = 'modifier'
    EVAL_CONDITION = 'condition'

    EVAL_CONDITION_ANY = 'any'
    EVAL_CONDITION_MATCH = 'match'

    EVAL_WILDCHAR = 'has_wildchar'

    def _is_modifier(self, char):
        return char in ['*', '?', '+']

    def evaluate(self, tokens):
        evaluations = []
        for token in tokens:
            token_eval = self._evaluate_token(token)
            token_eval = self._evaluate_condition(token_eval)
            token_eval = self._evaluate_wildchar(token_eval)
            evaluations.append(token_eval)

        return evaluations

    def _evaluate_token(self, token):
        eval = {}

        last_char = token[-1]
        if self._is_modifier(last_char):
            eval.update({Evaluator.EVAL_TOKEN: token[:-1], Evaluator.EVAL_MODIFIER: last_char, Evaluator.EVAL_CONDITION: None})
        else:
            eval.update({Evaluator.EVAL_TOKEN: token, Evaluator.EVAL_MODIFIER: None, Evaluator.EVAL_CONDITION: None})

        return eval

    def _evaluate_condition(self, eval):
        if eval[Evaluator.EVAL_TOKEN][0] == '[':
            eval[Evaluator.EVAL_TOKEN] = eval[Evaluator.EVAL_TOKEN][1:-1]
            eval[Evaluator.EVAL_CONDITION] = Evaluator.EVAL_CONDITION_ANY
        elif eval[Evaluator.EVAL_TOKEN][0] == '(':
            eval[Evaluator.EVAL_TOKEN] = eval[Evaluator.EVAL_TOKEN][1:-1]
            eval[Evaluator.EVAL_CONDITION] = Evaluator.EVAL_CONDITION_MATCH

        return eval

    def _evaluate_wildchar(self, eval):
        if '.' in eval[Evaluator.EVAL_TOKEN] and eval[Evaluator.EVAL_CONDITION] != Evaluator.EVAL_CONDITION_ANY:
            eval[Evaluator.EVAL_WILDCHAR] = True
        else:
            eval[Evaluator.EVAL_WILDCHAR] = False

        return eval