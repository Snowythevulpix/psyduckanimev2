import os

def edit_html_files(directory):
    replacement_text = '''
        <title>PsyduckAnime - watch Pokemon Diamond and Pearl for free </title>
        <meta property="og:title" content="Psyduckanime - watch pokemon for free">
        <meta property="og:image" content="https://m.media-amazon.com/images/M/MV5BMGNjMmFlYWUtMTBjNS00YzdlLTk3NzktZjFjMjZlMWFiODUyXkEyXkFqcGdeQXVyOTA1ODU0Mzc@._V1_FMjpg_UX1000_.jpg">
        <!-- Favicon -->
        <link rel="icon" href="https://m.media-amazon.com/images/M/MV5BMGNjMmFlYWUtMTBjNS00YzdlLTk3NzktZjFjMjZlMWFiODUyXkEyXkFqcGdeQXVyOTA1ODU0Mzc@._V1_FMjpg_UX1000_.jpg" />'''

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                content = file.read()

            edited_content = content.replace(
                '<title>PsyduckAnime - best place to watch pokemon subbed and dubbed</title>',
                replacement_text
            )

            with open(file_path, "w") as file:
                file.write(edited_content)

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    edit_html_files(current_directory)
    print("HTML files edited successfully.")
