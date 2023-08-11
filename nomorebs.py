import os
import fileinput

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Iterate through all .html files in the current directory
for root, dirs, files in os.walk(current_directory):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            
            # Perform the modification using fileinput module
            with fileinput.FileInput(file_path, inplace=True) as f:
                for line in f:
                    # Check if the line contains a <body> tag
                    if '<body' in line:
                        # Add dark-mode class to the body tag
                        modified_line = line.replace('<body', '<body class="dark-mode"')
                        print(modified_line, end='')
                    else:
                        print(line, end='')
