from matchers.matcher import Matcher


class MatchFinder:

    def setMatchers(self, matchers):
        self._matchers = matchers

    def _all_matchers_reported_ok(self, matchers_count):
        return matchers_count == len(self._matchers)

    def _match_iterator(self, text):
        text_len = len(text)
        match_begin_index = 0
        match_end_index = match_begin_index

        while match_begin_index < text_len:

            # as a single matcher represents only a fragment of whole RegEx
            # we need to iterate through all matchers
            matchers_reported_ok = 0
            for matcher in self._matchers:
                match = matcher.match(text[match_end_index:])

                if match:
                    matchers_reported_ok += 1
                    match_end_index += match['length']
                else:
                    break

            if self._all_matchers_reported_ok(matchers_reported_ok):
                found_match = [match_begin_index, match_end_index - 1]
                yield found_match

                match_begin_index = match_end_index
                match_end_index = match_begin_index
            else:
                match_begin_index += 1
                match_end_index = match_begin_index


    def findFirst(self, text):

        try:
            match = self._match_iterator(text).next()
        except StopIteration:
            match = None

        return match


    def findAll(self, text):

        result = []
        for match in self._match_iterator(text):
            result.append(match)

        return result