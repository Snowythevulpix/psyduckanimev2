import os
from bs4 import BeautifulSoup

def remove_next_episode_button(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')

        # Find and remove the button with the 'onclick' attribute set to 'nextEpisode()'
        button_tags = soup.find_all('button', {'onclick': 'nextEpisode()'})
        for button_tag in button_tags:
            button_tag.extract()  # Remove the button element

    with open(file_path, 'w') as file:
        file.write(str(soup))

def remove_next_episode_button_from_specific_files(directory):
    specific_files = ['home.html', 'discord.html', 'test.html', 'index.html']

    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name in specific_files and file_name.endswith('.html'):
                file_path = os.path.join(root, file_name)
                remove_next_episode_button(file_path)
                print(f"Removed 'Next Episode' button from {file_path}")

if __name__ == "__main__":
    target_directory = "."  # Change this to the directory containing your HTML files
    remove_next_episode_button_from_specific_files(target_directory)
