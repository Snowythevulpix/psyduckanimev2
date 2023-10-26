import os
import re
import chardet

# Define the directory path as the current working directory
directory_path = os.getcwd()

# Define the old and new URLs
old_url = "https://m.media-amazon.com/images/m/MV5BMGNjMmFlYWUtMTBjNS00YzdlLTk3NzktZjFjMjZlMWFiODUyXkEyXkFqcGdeQXVyOTA1ODU0Mzc@._V1_FMjpg_UX1000_.jpg"
new_url = "https://psyduckanime.lol/Psyduck.png"

# Define a function to replace URLs in an HTML file
def replace_urls_in_html_file(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    with open(file_path, 'r', encoding=encoding) as file:
        file_contents = file.read()
        new_contents = re.sub(re.escape(old_url), new_url, file_contents)
    
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(new_contents)

# Process only HTML files in the current directory and its subdirectories
for root, dirs, files in os.walk(directory_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        
        # Check if the file has an HTML extension (you can add more extensions if needed)
        if file_name.endswith('.html') or file_name.endswith('.htm'):
            try:
                replace_urls_in_html_file(file_path)
                print(f"Replaced URLs in {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")

print("URL replacement for HTML files complete.")
