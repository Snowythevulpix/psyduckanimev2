import os

# Directory path
directory_path = r'C:\Users\Hayle\OneDrive\Desktop\psyduckanime v2\psyduckanime-main\dub\os'

# Iterate through files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    # Check if the file is not 'home.html' and has a '.html' extension
    if os.path.isfile(file_path) and filename != 'home.html' and filename.endswith('.html'):
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the file content
            file_content = file.read()

            # Replace the line with the desired code
            file_content = file_content.replace('var episodeId = "pokemon-2019-dub-episode-133";',
                                                f'var episodeId = "pokemon-dub-episode-{filename[2:-5]}";')

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_content)

print("Modification completed.")
