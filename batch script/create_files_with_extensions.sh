#!/bin/bash

function create_files_with_extensions() {
    local dir_to_create="$1"
    local file_extensions=("${@:2}") # Use all the arguments after the first as the file extensions

    for ((i = 0; i < 5; i++)); do
        for ((j = 0; j < ${#file_extensions[@]}; j++)); do
            file_name="$dir_to_create/$i${file_extensions[$j]}"
            output=$(touch "$file_name")
            if [ ${#output} -ne 0 ]; then
                echo "$output"
            else
                echo "Hello World!" > "$file_name"
            fi
        done
    done

    return 0
}

# Example usage:
dir_to_create="logs"
file_extensions=(".txt" ".docx" ".log")
create_files_with_extensions "$dir_to_create" "${file_extensions[@]}"
