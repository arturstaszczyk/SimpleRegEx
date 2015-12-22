class Tokenizer:

    def tokenize(self, exp):
        tokens = []
        buffer = ""
        closing_element = None

        for current_char in exp:

            if self._is_special(current_char):
                tokens[-1] += current_char # based on assumption of correct input

            elif self._is_clustering(current_char):
                closing_element = ']' if current_char == '[' else ')'
                buffer = buffer + current_char

            else:
                if closing_element != None:
                    buffer = buffer + current_char
                    if closing_element == current_char:
                        tokens.append(buffer)
                        closing_element = None
                        buffer = ""
                else:
                    tokens.append(current_char)
        if buffer:
            tokens.append(buffer)

        return tokens

    def _is_special(self, char):
        return char in ['?', '*', '+']

    def _is_clustering(self, char):
        return char in ['(', '[']
