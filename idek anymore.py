import os
from bs4 import BeautifulSoup

# Function to replace the specified HTML content
def replace_content_in_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the <img> tag with the specified src attribute
    img_tag = soup.find('img', src='file:///C:/Users/Hayle/OneDrive/Desktop/psyduckanime%20v2/psyduckanime-main/Psyduck.png')

    # If the img_tag is found, replace its src attribute
    if img_tag:
        img_tag['src'] = 'https://psyduckanime.lol/Psyduck.png'

        # Save the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

# Traverse through the current directory and its subdirectories
for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('home.html'):
            file_path = os.path.join(root, file)
            replace_content_in_html(file_path)
            print(f'Replaced content in {file_path}')

print('Replacement completed.')
