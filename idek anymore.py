import os

def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        file_content = file.read()
    
    modified_content = file_content.replace(old_text, new_text)
    
    with open(file_path, 'w') as file:
        file.write(modified_content)

def search_and_replace_in_directory(directory_path, old_text, new_text):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".html"):  # Check for HTML files
                file_path = os.path.join(root, file_name)
                try:
                    replace_text_in_file(file_path, old_text, new_text)
                    print(f"Modified: {file_path}")
                except Exception as e:
                    print(f"Error modifying {file_path}: {e}")

if __name__ == "__main__":
    directory_path = os.path.abspath(os.getcwd())
    old_text = "https://c.delusionz.xyz/"
    new_text = "https://psyduckanime.xyz"
    
    search_and_replace_in_directory(directory_path, old_text, new_text)
