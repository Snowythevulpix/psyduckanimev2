import os

# The HTML code to be added
download_button_code = '''
<button onclick="redirectToDownload()">Click here to download</button>
<script>
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
</script>
'''

# Directory containing HTML files
DIRECTORY_PATH = './'  # Modify this to your desired directory path

def add_download_button(file_path):
    with open(file_path, 'r+') as file:
        content = file.read()
        if download_button_code in content:
            print(f"{file_path} already has download button")
        else:
            file.write(download_button_code)
            print(f"{file_path} now has a download button")

def process_html_files(directory_path):
    for file in os.listdir(directory_path):
        if file.endswith('.html'):
            file_path = os.path.join(directory_path, file)
            add_download_button(file_path)

if __name__ == '__main__':
    process_html_files(DIRECTORY_PATH)

    print("done")
