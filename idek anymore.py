import os
from bs4 import BeautifulSoup

def remove_dark_mode_text(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Find and remove the element containing the dark mode text
    dark_mode_text_element = soup.find(id="DarkModetext")
    if dark_mode_text_element:
        dark_mode_text_element.decompose()

    # Save the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(str(soup))

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))

    for root, _, files in os.walk(current_directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                remove_dark_mode_text(file_path)
                print(f"Removed dark mode text from: {file_path}")
