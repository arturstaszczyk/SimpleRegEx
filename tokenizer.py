class Tokenizer:

    def tokenize(self, exp):
        tokens = []
        buffer = ""
        end_element = None

        for x in exp:

            if self._is_special(x):
                tokens[-1] += x # based on assumption of correct input

            elif self._is_clustering(x):
                end_element = ']' if x == '[' else ')'
                buffer = buffer + x

            else:
                if end_element != None:
                    buffer = buffer + x
                    if end_element == x:
                        tokens.append(buffer)
                        end_element = None
                        buffer = ""
                else:
                    tokens.append(x)
        if buffer:
            tokens.append(buffer)

        return tokens

    def _is_special(self, char):
        return char in ['?', '*', '+']

    def _is_clustering(self, char):
        return char in ['(', '[']
