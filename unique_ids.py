import os
import re
import random

'''
Give the project directory to the path variable and run.
Then manually clear the ids assigned to components that already have ids 
(Error: No duplicate props allowed, react/jsx-no-duplicate-props).
'''

# Generate a random unique string for valid tag name
def generate_random_string(length=10):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(letters) for i in range(length))

# Define the regex: any word character starting with a capital letter followed by \b word boundary
regex = r'<([A-Z][a-zA-Z0-9.]*)'

# Path to the directory to be processed
path = '/Users/faruk.ulutas/Desktop/central/services/frontend/src'

# Iterate over each file in the directory and process it
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.js') or file.endswith('.jsx'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                # Read file line by line
                lines = f.readlines()
                for i, line in enumerate(lines):
                    # Check if "<" character is in the line
                    if "<" in line:
                        # Add whitespace before ">" character if it exists before splitting the line
                        line = re.sub(r'(?<=[^ ])>', ' >', line)
                        # To avoid syntax error translate these / > expressions to />
                        line = line.replace('/ >', '/>')
                        # To avoid syntax error translate these / > expressions to />
                        line = line.replace('= >', '=>')
                        # Split the line by whitespace character
                        words = line.split(" ")
                        # Check if any word contains the regex and doesn't contain 'id'
                        for word in words:
                            if not re.search(r'\bid\b', word) and not '</' in word and re.search(regex, word):
                                # Generate a random unique string and add id to the tag
                                unique_id = generate_random_string()
                                match = re.search(regex, word)
                                new_word = re.sub(match.group(1), f"{match.group(1)} id='{unique_id}'", word)
                                line = line.replace(word, new_word)
                        lines[i] = line
            # Overwrite the file with the modified content
            with open(filepath, 'w') as f:
                f.writelines(lines)
