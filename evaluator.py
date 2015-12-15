class Evaluator:

    def _is_modifier(self, char):
        return char in ['*', '?', '+']

    def evaluate(self, tokens):
        evaluations = []
        for token in tokens:
            token_eval = self.evaluate_token(token)
            token_eval = self.evaluate_condition(token_eval)
            evaluations.append(token_eval)

        return evaluations

    def evaluate_token(self, token):
        eval = {}

        last_char = token[-1]
        if self._is_modifier(last_char):
            eval.update({'token': token[:-1], 'modifier': last_char, 'condition': None})
        else:
            eval.update({'token': token, 'modifier': None, 'condition': None})

        return eval

    def evaluate_condition(self, eval):
        if eval['token'][0] == '[':
            eval['token'] = eval['token'][1:-1]
            eval['condition'] = 'any'
        elif eval['token'][0] == '(':
            eval['token'] = eval['token'][1:-1]
            eval['condition'] = 'match'

        return eval;