import os
import fileinput
import re

# Get user input for the episode ID and directory to be edited
episode_id = input("Enter the episode ID: ")
directory = input("Enter the directory path to be edited: ")

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html") and file != "home.html":
            file_path = os.path.join(root, file)
            episode_match = re.search(r'ep(\d+)\.html', file)
            if episode_match:
                episode_number = episode_match.group(1)
                with open(file_path, 'r', encoding='utf-8') as original_file:
                    content = original_file.read()
                    modified_content = re.sub(r'var episodeId = "pokemon-sun-moon-episode-\d+";', f'var episodeId = "{episode_id}-{episode_number}";', content)
                with open(file_path, 'w', encoding='utf-8') as modified_file:
                    modified_file.write(modified_content)
                print(f"Modified: {file_path}")
