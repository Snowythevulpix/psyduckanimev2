import os
import webbrowser

def search_google(query):
    uppercase_query = query.upper()
    search_url = f"https://www.google.com/search?q={uppercase_query}"
    webbrowser.open_new_tab(search_url)

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.realpath(__file__))
    last_directory_name = os.path.basename(script_directory)
    search_google(last_directory_name)
