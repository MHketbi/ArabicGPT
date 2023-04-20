import json

input_file = "quran-simple-clean.txt"
output_file = "MegatronReady.json"

with open(input_file, "r", encoding="utf-8") as in_file, open(output_file, "w", encoding="utf-8") as out_file:
    for line in in_file:
        line = line.strip()  # Remove any leading and trailing whitespaces
        json_line = {"src": "quran-simple-clean", "text": f'"{line}"'}
        out_file.write(json.dumps(json_line) + "\n")
