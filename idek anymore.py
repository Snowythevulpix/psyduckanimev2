import os
from bs4 import BeautifulSoup

# New logo URL
new_logo_url = "https://vulpix500.gay/Psyduck.png"

# Traverse the directory tree and process each HTML file
for root, _, files in os.walk("."):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            
            # Read the original HTML file
            with open(filepath, "r", encoding="utf-8") as file:
                original_html = file.read()
            
            # Parse the HTML using Beautiful Soup
            soup = BeautifulSoup(original_html, "html.parser")
            
            # Find and update the logo img tag
            logo_img = soup.find("img", class_="logo")
            if logo_img:
                logo_img["src"] = new_logo_url
            
            # Write the modified HTML back to the file
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(str(soup))
            
            print(f"Logo updated in {filepath}")
