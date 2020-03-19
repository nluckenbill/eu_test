import os
from bs4 import BeautifulSoup
import glob
import re

# Python regex to clean up html parts missed
regex = r"(?=title=)(.*?)(?<=\/\>)"
# Replace with
subst = ""

# Find MD files

for filepath in glob.iglob('./post/2014-10-29-deluge-lake-east-vail.md', recursive=True):
    with open(filepath, encoding='utf8') as file:
        html = file.read()
    raw = BeautifulSoup(html).get_text()

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