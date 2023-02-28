#!/bin/bash

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

echo "Type name of the folder:"
read -r dir_to_search

echo "Type name of the file extension:"
read -r extension

file_names=($(find_files_with_extension "$dir_to_search" "$extension"))
for file_name in "${file_names[@]}"; do
    echo "path: $file_name"
    echo "base name: $(basename $file_name)"
done

exit 0
