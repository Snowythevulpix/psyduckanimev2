import os
import fileinput
import re

def update_files(directory, episode_id, base_ep1_path, excluded_folder):
    for root, dirs, files in os.walk(directory):
        if excluded_folder in dirs:
            dirs.remove(excluded_folder)  # Skip the excluded folder
        for file in files:
            if file == "ep1.html":
                file_path = os.path.join(root, file)
                update_script(file_path, episode_id, base_ep1_path)

def update_script(file_path, episode_id, base_ep1_path):
    print(f"Updating file: {file_path} with episodeId: {episode_id}")
    
    with open(file_path, 'r', encoding='utf-8') as ep1_file:
        ep1_content = ep1_file.read()

    with open(base_ep1_path, 'r', encoding='utf-8') as base_ep1_file:
        base_ep1_content = base_ep1_file.read()

    # Replace the content of the file with base ep1 content
    with open(file_path, 'w', encoding='utf-8') as modified_file:
        modified_file.write(base_ep1_content)

    # Update the episodeId variable
    with open(file_path, 'r', encoding='utf-8') as original_file:
        content = original_file.read()

    modified_content = re.sub(r'var episodeId = "pokemon-sun-moon-episode-\d+";', f'var episodeId = "{episode_id}-1";', content)

    with open(file_path, 'w', encoding='utf-8') as modified_file:
        modified_file.write(modified_content)

    print(f"Modified: {file_path}")

# Predefined episode ID and base ep1 path
episode_id = "your_episode_id"  # Replace with the desired episode ID
base_ep1_path = r'C:\Users\Hayle\OneDrive\Desktop\psyduckanime v2\psyduckanime-main\dub\sm\ep1.html'

# Directory to search for ep1.html files
base_directory = r'C:\Users\Hayle\OneDrive\Desktop\psyduckanime v2\psyduckanime-main\sub\sm'

# Folder to exclude (e.g., "xy")
excluded_folder = "xy"

update_files(base_directory, episode_id, base_ep1_path, excluded_folder)
