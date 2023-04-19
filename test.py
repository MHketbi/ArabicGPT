import os

data_folder = "C:\\Git\\ArabicGPT\\Data"
output_filename = "DATA.txt"

def append_txt_to_file(input_txt, output_txt_filename):
    with open(input_txt, 'r', encoding='utf-8') as txt_file:
        content = txt_file.read()

    with open(output_txt_filename, 'a', encoding='utf-8') as output_file:
        output_file.write(content)
        output_file.write('\n\n\n')

def process_directory(directory, output_txt_filename):
    for entry in os.scandir(directory):
        if entry.is_file() and entry.name.endswith(".txt"):
            append_txt_to_file(entry.path, output_txt_filename)
        elif entry.is_dir():
            process_directory(entry.path, output_txt_filename)

with open(output_filename, 'w', encoding='utf-8') as output_file:
    # This line creates an empty DATA.txt file or clears its content if it already exists
    pass

process_directory(data_folder, output_filename)
