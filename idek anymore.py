import os
from bs4 import BeautifulSoup

# HTML template for the top bar
top_bar_template = """
<div class="top-bar">
    <a href="https://snowythevulpix.github.io/redirect" title="Go to Home">
        <img class="logo" src="file:///C:/Users/Hayle/OneDrive/Desktop/psyduckanime%20v2/psyduckanime-main/Psyduck.png" alt="Logo"/>
    </a>
    PsyduckAnime - watch pokemon subbed and dubbed for free
</div>
"""

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
            
            # Remove any existing top bars
            for top_bar in soup.find_all(class_="top-bar"):
                top_bar.extract()
            
            # Create the top bar tag
            top_bar_tag = soup.new_tag("div")
            top_bar_tag["class"] = "top-bar"
            a_tag = soup.new_tag("a", href="https://snowythevulpix.github.io/redirect", title="Go to Home")
            img_tag = soup.new_tag("img", class_="logo", src="file:///C:/Users/Hayle/OneDrive/Desktop/psyduckanime%20v2/psyduckanime-main/Psyduck.png", alt="Logo")
            img_tag["style"] = "width: 40px; height: 40px; padding: 5px; cursor: pointer;"  # Apply logo size and padding
            a_tag.append(img_tag)
            top_bar_tag.append(a_tag)
            top_bar_tag.append("PsyduckAnime - watch pokemon subbed and dubbed for free")
            
            # Insert the top bar template at the beginning of the body
            body_tag = soup.body
            body_tag.insert(0, top_bar_tag)
            
            # Write the modified HTML back to the file
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(str(soup))
            
            print(f"Top bar added to {filepath}")
