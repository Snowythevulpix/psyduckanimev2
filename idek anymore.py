import os
from bs4 import BeautifulSoup

# New logo URL
new_logo_url = "https://psyduckanime.lol/Psyduck.png"

# Function to update image source URL
def update_logo_in_html_file(file_path):
    try:
        # Read the original HTML file
        with open(file_path, "r", encoding="utf-8") as file:
            original_html = file.read()

        # Parse the HTML using Beautiful Soup
        soup = BeautifulSoup(original_html, "html.parser")

        # Find and update the logo img tag
        logo_img = soup.find("img", class_="logo")
        if logo_img:
            logo_img["src"] = new_logo_url

        # Write the modified HTML back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(soup))

        print(f"Logo updated in {file_path}")

    except Exception as e:
        print(f"Error updating logo in {file_path}: {e}")

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Recursively traverse the current directory and its subdirectories
for root, _, files in os.walk(current_directory):
    for filename in files:
        if filename == "home.html":
            filepath = os.path.join(root, filename)
            update_logo_in_html_file(filepath)
