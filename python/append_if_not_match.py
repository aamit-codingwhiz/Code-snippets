import re

def append_if_not_match(string, patterns):
    """
    Appends "$$" to the end of a string if the last two characters do not match
    any of the specified patterns.
    """
    status = True
    for pattern in patterns:
        if re.search(pattern, string[-2:]):
            status = False
            break
    if status:
        string += "$$"
    return string

# Example usage
string1 = "hi, how are you$?$"
patterns1 = ["\$\$", "!\$", "\?\$", "\$$"]
string1 = append_if_not_match(string1, patterns1)
print(string1)

string2 = "গাজা খা তাহলে"
# patterns2 = ["\$\$", "!\$", "\?\$", "\$$"]
patterns2 = ["\\$\\$", "!\\$", "\\?\\$", "\\$\\$", "।\\$", "!", "\\?","।"]
string2 = append_if_not_match(string2, patterns2)
print(string2)
