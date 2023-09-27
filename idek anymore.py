import os
import fileinput
import re

# Read the content of ep2.html
with open(r'C:\Users\Hayle\OneDrive\Desktop\psyduckanime v2\psyduckanime-main\sub\sm\ep2.html', 'r', encoding='utf-8') as ep2_file:
    ep2_content = ep2_file.read()

directory = r'C:\Users\Hayle\OneDrive\Desktop\psyduckanime v2\psyduckanime-main\sub\sm'

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html") and file != "home.html":
            file_path = os.path.join(root, file)
            episode_match = re.search(r'ep(\d+)\.html', file)
            if episode_match:
                episode_number = episode_match.group(1)
                modified_content = ep2_content.replace('pokemon-sun-moon-episode-2', f'pokemon-sun-moon-episode-{episode_number}')
                with open(file_path, 'w', encoding='utf-8') as modified_file:
                    modified_file.write(modified_content)
                print(f"Modified: {file_path}")
