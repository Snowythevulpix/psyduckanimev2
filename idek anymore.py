import os
from bs4 import BeautifulSoup

# Traverse the directory tree and process each HTML file
for root, _, files in os.walk("."):
    for filename in files:
        if filename == "home.html":
            filepath = os.path.join(root, filename)

            # Read the original HTML file
            with open(filepath, "r", encoding="utf-8") as file:
                original_html = file.read()

            # Parse the HTML using Beautiful Soup
            soup = BeautifulSoup(original_html, "html.parser")

            # Find and remove the specific text
            text_to_remove = "PsyduckAnime - watch pokemon subbed and dubbed for free"
            text_elements = soup.find_all(text=True)
            for element in text_elements:
                if text_to_remove in element:
                    element.replace_with("")

            # Write the modified HTML back to the file
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(str(soup))

            print(f"Text removed from {filepath}")
