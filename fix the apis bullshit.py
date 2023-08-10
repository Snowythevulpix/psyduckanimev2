import os
import re

def replace_url_in_files(directory, old_url, new_url):
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'r', encoding='utf-8', errors='replace') as file:
                    content = file.read()

                # Perform the replacement using regular expressions
                new_content = re.sub(re.escape(old_url), new_url, content)

                # Write the modified content back to the file
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)

if __name__ == "__main__":
    # Replace these values with the old URL and the new URL you want to use
    old_url = "https://api.consumet.org/"
    new_url = "https://api.consumet.org/"

    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Call the function to replace the URLs in all files within the directory
    replace_url_in_files(current_directory, old_url, new_url)

print("done")
