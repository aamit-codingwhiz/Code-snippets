def longest_common_contiguous_subsequence(list1, list2):
    m = len(list1)
    n = len(list2)

    # Create a matrix to store the lengths of common contiguous subsequences
    lccs = [[0] * (n+1) for i in range(m+1)]
    max_length = 0
    ending_index = 0

    # Fill in the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if list1[i-1] == list2[j-1]:
                lccs[i][j] = lccs[i-1][j-1] + 1

                # Check if the current subsequence is the longest so far
                if lccs[i][j] > max_length:
                    max_length = lccs[i][j]
                    ending_index = i-1
            else:
                lccs[i][j] = 0

    # Extract the longest common contiguous subsequence from list1
    if max_length == 0:
        return []

    start_index = ending_index - max_length + 1
    return list1[start_index:ending_index+1]

list1 = ["apple", "banana", "orange", "grape", "kiwi"]
list2 = ["banana", "kiwi", "orange", "grape"]
lccs = longest_common_contiguous_subsequence(list1, list2)
print(lccs)
