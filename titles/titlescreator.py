import json

# File paths
input_file = r'C:\Users\Hayle\psyduckanimev2\titles\titles.txt'
output_file = r'C:\Users\Hayle\psyduckanimev2\titles\sm.json'

# Read data from smtitles.txt and process
episode_data = {}
with open(input_file, 'r', encoding='latin-1', errors='ignore') as file:  # Try reading with latin-1 encoding
    for line in file:
        parts = line.strip().split('|')
        episode_id = parts[1].replace('SM', '')
        episode_data[episode_id] = {
            "ID": int(episode_id),
            "EnglishTitle": parts[2],
            "JapaneseTitle": parts[3],
            "JapaneseTransliteration": parts[4],
            "AirDate": {
                "International": parts[5],
                "Japanese": parts[6]
            }
        }

# Check if data was read correctly
print("Number of episodes processed:", len(episode_data))

# Write formatted data to smtitles.json with ensure_ascii=False
try:
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(episode_data, json_file, indent=2, ensure_ascii=False)
    print("Data successfully written to smtitles.json")
except Exception as e:
    print("Error writing data:", e)
