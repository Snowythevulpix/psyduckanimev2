import os

# Directory containing HTML files
DIRECTORY_PATH = './'  # Modify this to your desired directory path

def replace_strings_in_file(file_path, old_string, new_string):
    with open(file_path, 'r') as file:
        content = file.read()

    new_content = content.replace(old_string, new_string)

    with open(file_path, 'w') as file:
        file.write(new_content)

def process_html_files(directory_path, old_string, new_string):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                replace_strings_in_file(file_path, old_string, new_string)

if __name__ == '__main__':
    old_string = "https://consumet-api-production-0afb.up.railway.app"
    new_string = "https://c.delusionz.xyz"

    process_html_files(DIRECTORY_PATH, old_string, new_string)
