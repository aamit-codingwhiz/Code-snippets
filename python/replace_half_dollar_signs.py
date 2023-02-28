def replace_half_dollar_signs(s):
    """
    This function takes a string s as input, splits it into words, 
    and replaces half of the dollar signs in each word with an asterisk. 
    The modified words are then joined back into a string and returned.
    """

    def contains_only_dollar_signs(s):
        for char in s:
            if char != '$':
                return False
        return True
    
    s2 = s.split()
    for i in range(len(s2)):
        if contains_only_dollar_signs(s2[i]):
            dollar_count = s2[i].count('$')
            s2[i] = s2[i][:(dollar_count//2)] + '*' + s2[i][(dollar_count//2):]
    return " ".join(s2)

# example
s1 = "$$ তুলতে হল।"
s2 = replace_half_dollar_signs(s1)
print(s2)
