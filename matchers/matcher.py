from abc import ABCMeta, abstractmethod


class Matcher:

    __metaclass__ = ABCMeta

    KEY_MATCH_LENGTH = 'length'

    @abstractmethod
    def match(self):
        pass

    def _modify_result_by_modifier(self, result, modifier):
        if modifier == '*':
            return result
        elif modifier == '?':
            return min(result, 1)
        elif modifier == '+':
            return result if result > 0 else None
        else:
            return min(result, 1) if result > 0 else None