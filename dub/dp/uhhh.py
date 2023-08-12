import os
import fileinput

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# URL replacements
old_url = "https://consumet-api-production-0afb.up.railway.app"
new_url = "https://c.delusionz.xyz"

# Iterate through all .html files in the current directory
for root, dirs, files in os.walk(current_directory):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            
            # Perform the replacement using fileinput module
            with fileinput.FileInput(file_path, inplace=True) as f:
                for line in f:
                    print(line.replace(old_url, new_url), end='')
