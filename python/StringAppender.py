import re

class StringAppender:
    """
    A class for appending "$$" to the end of a string if the last two characters
    do not match any of the specified patterns.
    """

    def __init__(self, patterns):
        """
        Initializes a new StringAppender object.

        :param patterns: A list of regex patterns to check against the last two
                         characters of a string.
        :type patterns: list[str]
        """
        self.patterns = patterns

    def append_if_not_match(self, string):
        """
        Appends "$$" to the end of a string if the last two characters do not
        match any of the specified patterns.

        :param string: The input string to check.
        :type string: str
        :return: The modified string with "$$" appended if necessary.
        :rtype: str
        """
        status = True
        for pattern in self.patterns:
            if re.search(pattern, string[-2:]):
                status = False
                break
        if status:
            string += "$$"
        return string

    
# example usage
patterns1 = ["\$\$", "!\$", "\?\$", "\$$"]
appender1 = StringAppender(patterns1)
string1 = "hi, how are you$?$"
string1 = appender1.append_if_not_match(string1)
print(string1)

patterns2 = ["\\$\\$", "!\\$", "\\?\\$", "\\$\\$", "।\\$", "!", "\\?","।"]
appender2 = StringAppender(patterns2)
string2 = "গাজা খা তাহলে"
string2 = appender2.append_if_not_match(string2)
print(string2)
