class BadMatcher(Exception):
    def __str__(self):
        return "Bad matcher was used to match the regex"

class BadCondition(Exception):
    def __str__(self):
        return "Condition used '[any]' or '(match)' is invalid with given token"

class NoModifier(Exception):
    def __str__(self):
        return "No modifier '*', '+', '?' was used for a (match) condition"
