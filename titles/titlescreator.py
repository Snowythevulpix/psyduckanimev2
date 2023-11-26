import json

def create_json_from_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = []
    start_processing = False
    for line in lines:
        if '{{Episodelistbody' in line:
            start_processing = True
            continue

        if start_processing:
            episode_data = line.strip().split('|')
            if len(episode_data) >= 5:
                episode_info = {
                    "Episode Number": episode_data[0],
                    "English Title": episode_data[1],
                    "Japanese Title": episode_data[2],
                    "Air Date (Japan)": episode_data[3],
                    "Air Date (US)": episode_data[4]
                }
                data.append(episode_info)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)

# Replace 'titles.txt' with your file's path and name
# Replace 'sm.json' with the desired output JSON file's path and name
create_json_from_file(r'C:\Users\Hayle\psyduckanimev2\titles\titles.txt', r'C:\Users\Hayle\psyduckanimev2\titles\sm.json')
