import sys
import re

repo_name = sys.argv[1]

with open('README.md', 'r') as f:
    readme = f.read()
    readme = re.sub('lola', repo_name, readme)

with open('README.md', 'w') as f:
    f.write(readme)
