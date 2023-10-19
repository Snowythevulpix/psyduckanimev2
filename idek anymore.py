import os

# Directory path to start the search and replace
start_directory = os.path.dirname(__file__)  # Use the directory of the script

# Replace this string
search_string = "https://c.delusionz.xyz"

# Replace with this string
replace_string = "https://psyduckanime.xyz"

# Function to search and print changes without modifying the file
def search_and_print_changes(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            modified_line = line.replace(search_string, replace_string)
            if modified_line != line:
                print(f"Modifying {file_path}: {line.strip()} -> {modified_line.strip()}")
    
# Recursively traverse the directory and its subdirectories
for root, dirs, files in os.walk(start_directory):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.isfile(file_path):
            search_and_print_changes(file_path)

print("Search and print changes complete.")
