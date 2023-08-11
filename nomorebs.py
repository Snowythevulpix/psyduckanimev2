import os

def replace_directory_in_url(url, search, replace):
    # Split the URL into parts
    parts = url.split('/')

    # Replace the search string with the replace string
    modified_parts = [replace if part == search else part for part in parts]

    # Reconstruct the modified URL
    modified_url = '/'.join(modified_parts)

    return modified_url

# List of directory URLs
directory_urls = [
    "https://consumet-api-production-0afb.up.railway.app/dir1/",
    "https://consumet-api-production-0afb.up.railway.app/dir2/subdir/",
    # Add more URLs as needed
]

search_string = "https://consumet-api-production-0afb.up.railway.app"
replace_string = "https://c.delusionz.xyz"

# Replace directories in each URL
modified_urls = [replace_directory_in_url(url, search_string, replace_string) for url in directory_urls]

# Print the modified URLs
for modified_url in modified_urls:
    print(modified_url)
