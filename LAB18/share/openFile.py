import subprocess
import os

# Change directory to the path where your executable files are located
os.chdir('C:/Users/Administrator/Desktop/3EXEsmood')

# Create a list to hold the results from all executable files
results = []

# Loop through all files in the directory
for filename in os.listdir('.'):
    if filename.endswith('.exe'):
        # Run the executable file with input "18" using subprocess
        proc = subprocess.Popen([filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # Send input to the subprocess
        proc.stdin.write(b'18\n')
        proc.stdin.close()
        # Wait for the subprocess to finish and get its output
        result = proc.stdout.read()
        # Extract the string inside the parentheses and add it to the results
        result_str = result.decode('utf-8')
        start_index = result_str.find('(')
        end_index = result_str.find(')')
        if start_index != -1 and end_index != -1:
            results.append(result_str[start_index + 1:end_index])

# Write the concatenated results to a text file
with open('results.txt', 'w') as f:
    f.write(''.join(results))

print('Results written to results.txt')