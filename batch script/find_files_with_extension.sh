#!/bin/bash

# This function finds all files with a specified extension in a specified directory
# Arguments:
# 1. The name of the directory to search for files
# 2. The extension of the files to search for
# Returns:
# An array of the names of files found in the directory with the specified extension
function find_files_with_extension() {
    local dir_to_search="$1"
    local extension="$2"
    local file_names=()

    for file_name in "$dir_to_search"/*".$extension"; do
        if [ -f "$file_name" ]; then  # Check if the file exists and is a regular file
            file_names+=("$file_name")
        fi
    done
    echo "${file_names[@]}"
}

# Ask the user for input
echo "Type name of the folder:"
read -r dir_to_search

echo "Type name of the file extension:"
read -r extension

# Call the function and store the result in an array
file_names=($(find_files_with_extension "$dir_to_search" "$extension"))

# Print out the results
for file_name in "${file_names[@]}"; do
    echo "path: $file_name"
    echo "base name: $(basename $file_name)"
done

# Exit with status 0
exit 0
