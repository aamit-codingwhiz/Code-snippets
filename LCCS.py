import difflib

str1 = "ABCDer11GH"
str2 = "AEDer11FHR"

matcher = difflib.SequenceMatcher(None, str1, str2)
match = matcher.find_longest_match(0, len(str1), 0, len(str2))

lccs = str1[match.a:match.a+match.size]

print(lccs)
