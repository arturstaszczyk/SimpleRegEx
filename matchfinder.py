from matcher import Matcher


class MatchFinder:

    def setMatchers(self, matchers):
        self._matchers = matchers

    def findFirst(self, text):

        text_len = len(text)
        text_begin_index = 0
        text_check_index = text_begin_index
        result = None

        while text_begin_index < text_len:

            matchers_reported_ok = 0
            for matcher in self._matchers:
                match = matcher.match(text[text_check_index:])
                if match:
                    matchers_reported_ok += 1
                    text_check_index += match[Matcher.MATCH_LENGTH]
                else:
                    break

            if matchers_reported_ok == len(self._matchers):
                result = [text_begin_index, text_check_index]
                return result

            text_begin_index += 1
            text_check_index = text_begin_index

