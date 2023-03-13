input_file_path = 'blueprint.txt'
output_file_path = 'blueprint_output.txt'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        if 'Item("Craftplan_' in line:
            output_file.write(line[line.index('Item("Craftplan_'):])
