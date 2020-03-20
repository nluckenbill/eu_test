import os
from bs4 import BeautifulSoup
import glob
import re

# Python regex to clean up html parts missed
#regex = r"(?<=\")(.*\.jpg)"

# Replace with
subst = ""
pattern = re.compile(r"(?<=\")(.*\.jpg)", re.IGNORECASE)

# Find MD files

for filepath in glob.iglob('./content/post/**/*.md', recursive=True):
    if filepath:    
        with open(filepath, encoding='utf8') as file:
            contents = file.read()
            print(contents)
            for line in file:
                if pattern.search(line) != None:
                    print(line, end='')
    else:
        print("No files found")

# Remove whitespace
    clean_text = raw.rstrip().strip()

# Troubleshoot
#    print(filepath)

# Run Regex
    result = re.sub(regex, subst, clean_text, 0, re.DOTALL)

    if result:
        print (result)
    file.close()
#    s = s.replace('hello', 'world')
    with open(filepath, "w", encoding='utf8') as file:
        file.write(result)
        file.close