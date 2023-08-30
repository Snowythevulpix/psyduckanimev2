import os
from bs4 import BeautifulSoup

def remove_download_button(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Remove the download button if it exists
    download_button = soup.find("button", onclick="redirectToDownload()")
    if download_button:
        download_button.extract()

        # Save the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(str(soup))

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # List of files to exclude the download button from
    excluded_files = ["home.html", "index.html"]

    for root, _, files in os.walk(current_directory):
        for file in files:
            if file.endswith('.html') and file in excluded_files:
                file_path = os.path.join(root, file)
                remove_download_button(file_path)
                print(f"Removed download button from: {file_path}")
