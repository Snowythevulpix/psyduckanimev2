import os
from bs4 import BeautifulSoup

def add_download_button(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Check if the download button code is already present
    existing_download_button = soup.find("button", onclick="redirectToDownload()")
    if not existing_download_button:
        download_button = soup.new_tag("button")
        download_button["onclick"] = "redirectToDownload()"
        download_button.string = "Click here to download"

        script_tag = soup.new_tag("script")
        script_tag.string = """
            function redirectToDownload() {
                fetch('https://c.delusionz.xyz/anime/gogoanime/watch/' + episodeId)
                    .then(response => response.json())
                    .then(data => {
                        var downloadUrl = data.download;
                        window.location.href = downloadUrl;
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            }
        """

        # Add the download button and script to the end of the body
        body_tag = soup.find("body")
        body_tag.append(download_button)
        body_tag.append(script_tag)

        # Save the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(str(soup))

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))

    for root, _, files in os.walk(current_directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                add_download_button(file_path)
                print(f"Added download button to: {file_path}")
