# Define the HTML content to be inserted
loading_gif_block = '''
<div id="loading" style="display: block;">
    <!-- Display the loading GIF with a 16:9 aspect ratio -->
    <img src="https://psyduckanime.lol/loading.gif" alt="Loading..." style="height: 360px; width: 640px;">
</div>
'''

# Define the JavaScript code to hide the loading GIF after the episode is loaded
hide_loading_gif_script = '''
<script>
    // Function to hide the loading GIF
    function hideLoadingGif() {
        var loadingDiv = document.getElementById('loading');
        loadingDiv.style.display = 'none';
    }

    // Create a function to check if the episode is loaded
    function isEpisodeLoaded() {
        return new Promise((resolve) => {
            var player = getPlayer();
            player.on('play', function () {
                resolve();
            });
        });
    }

    // Call the hideLoadingGif function after the episode is loaded
    isEpisodeLoaded().then(hideLoadingGif);
</script>
'''

# Define the file path for ep1.html
file_path = r'C:\Users\Hayle\OneDrive\Desktop\psyduckanime v2\psyduckanime-main\sub\sm\ep1.html'

try:
    # Read the content of the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Find the insertion point for the loading GIF (just under the top bar definition)
    insertion_point = '<!-- Insert Loading GIF Here -->'
    modified_content = html_content.replace('PsyduckAnime - watch pokemon subbed and dubbed for free', 'PsyduckAnime - watch pokemon subbed and dubbed for free' + loading_gif_block, 1)

    # Find the insertion point for hide loading GIF script (right before </body>)
    insertion_point_script = '<!-- Insert JavaScript Here -->'
    modified_content = modified_content.replace('</body>', hide_loading_gif_script + '\n</body>', 1)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

    print(f"Updated {file_path}")
except FileNotFoundError:
    print(f"Error: File not found at path {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
