print('****************************************************************************************************')
print('files')
print('****************************************************************************************************')

import os
output_file = 'combined.py'
file_count = 1
with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in sorted(os.listdir(".")):
        if os.path.isfile(filename) and filename.endswith('.py') and  filename != output_file:
            with open(filename, 'r', encoding='utf-8') as current_file:
                file_content = current_file.read()
                outfile.write(file_content + '\n')
            file_count += 1

print("\n")
print(f'{output_file} combined {file_count} files')
print("\n")
