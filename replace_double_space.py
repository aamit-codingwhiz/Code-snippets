def replace_double_spaces(str1, str2):
    # split str1 by double spaces and str2 by single spaces
    str1_list = str1.split("  ")
    str2_list = str2.split()
    str2_list_copy = str2_list.copy()
    
    print("str1_list", str1_list)
    print("str2_list", str2_list)
    
    str2_list = [i.replace('$', '') for i in str2_list]
    print("str2_list", str2_list)
    
    # 
    str1_list_part1 = str1_list[0].split()
    print("str1_list_part1", str1_list_part1)
    
    for i in range(len(str1_list_part1)):
        if (str1_list_part1[i]==str2_list[i]):
            continue
        else:
            i = None
            break
    
    print("i", i)
    if i != None:
        output = " ".join(str2_list_copy[:i+1]) + " $ $" + " ".join(str2_list_copy[i+1:])
    else:
        output = str2
    return output

# example usage:
str1 = "abc bdc  pp"
str2 = "abc $$bdc pp"
output = replace_double_spaces(str1, str2)
print(output)
# expected output: "abc $$bdc $ $pp"


# str1 = 'আর মিডিয়া গুলো “বনসাই থেকে বটবৃক্ষ” টাইপ  চটুল নিউজ'
# str2 = 'আর $মিডিয়া গুলো$ “বনসাই থেকে বটবৃক্ষ” টাইপ চটুল নিউজ'
# output = replace_double_spaces(str1, str2)
# print(output)
