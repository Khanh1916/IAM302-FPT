import binascii
import os

search_start = b'\x3B\x05'
search_end = b'\x75\x1E'
replace_value = b'\x90\x90\x90\x90\x90\x90\x90\x90'

# Change directory to the path where your files are located
os.chdir('C:/Users/Administrator/Desktop/3EXEsmood')

# Loop through all files in the directory
for filename in os.listdir('.'):
    if filename.endswith('.exe') or filename.endswith('.dll'):
        # Open the file in binary mode
        with open(filename, 'rb') as f:
            file_contents = f.read()

        # Loop through the file contents searching for the hex pattern
        i = 0
        while i < len(file_contents):
            if file_contents[i:i+2] == search_start:
                j = i + 2
                while j < len(file_contents):
                    if file_contents[j:j+2] == search_end:
                        # Replace the hex pattern with the replacement value
                        file_contents = file_contents[:i] + replace_value + file_contents[j+2:]
                        break
                    j += 1
                break  # Remove this break if you want to replace all occurrences
            i += 1

        # Write the modified file contents back to the file
        with open(filename, 'wb') as f:
            f.write(file_contents)