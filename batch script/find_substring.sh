#!/bin/bash

# This function finds the index of the first occurrence of a substring in a string
# Usage: find_substring <string> <substring>
# Returns: The index of the first occurrence of the substring in the string, or -1 if not found
function find_substring() {
    string="$1"
    substring="$2"
    len_substring=${#substring}

    max_index=$(echo "${#string} - ${len_substring}" | bc )
    for (( i = 0; i <= max_index; i++ )); do
        if [ "${string:$i:${len_substring}}" == "$substring" ]; then
            echo $i
            return 0
        fi
    done

    echo "-1"
    return 1
}

# Example usage
index=$(find_substring "Hello World" "World")
echo "Substring found at index $index"
