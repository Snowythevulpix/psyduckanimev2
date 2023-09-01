import os
from bs4 import BeautifulSoup

# New logo URL
new_logo_url = "https://psyduckanime.lol/Psyduck.png"

# Function to update the logo URL in an HTML file
def update_logo_in_html_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            original_html = file.read()

        # Parse the HTML using Beautiful Soup
        soup = BeautifulSoup(original_html, "html.parser")

        # Find the specific line to replace
        target_line = '<body class="dark-mode"><div class="top-bar"><a href="https://snowythevulpix.github.io/redirect" title="Go to Home"><img alt="Logo" class_="logo" src="file:///C:/Users/Hayle/OneDrive/Desktop/psyduckanime%20v2/psyduckanime-main/Psyduck.png" style="width: 40px; height: 40px; padding: 5px; cursor: pointer;"/></a>PsyduckAnime - watch pokemon subbed and dubbed for free</div>'

        # Check if the target line is in the HTML file
        if target_line in str(soup):
            # Replace the target line with the new line
            new_line = f'<body class="dark-mode"><div class="top-bar"><a href="https://snowythevulpix.github.io/redirect" title="Go to Home"><img alt="Logo" class_="logo" src="{new_logo_url}" style="width: 40px; height: 40px; padding: 5px; cursor: pointer;"/></a>PsyduckAnime - watch pokemon subbed and dubbed for free</div>'
            original_html = original_html.replace(target_line, new_line)

            # Write the modified HTML back to the file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(original_html)

            print(f"Logo updated in {file_path}")
    except Exception as e:
        print(f"Error updating logo in {file_path}: {e}")

# Traverse the directory tree and process each HTML file
for root, _, files in os.walk("."):
    for filename in files:
        if filename.endswith(".html"):
            file_path = os.path.join(root, filename)
            update_logo_in_html_file(file_path)
