import os

def find_keyword_in_files(folder_path, keyword):
    with open('blueprint.txt', 'w') as output_file:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r') as input_file:
                    for line in input_file:
                        if keyword in line:
                            output_file.write(file_path + ': ' + line)

folder_path = r'Enter\path\to\folder\here'
keyword = 'Craftplan'
find_keyword_in_files(folder_path, keyword)















