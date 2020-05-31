import sys
import re

github_name = sys.argv[1]

with open('README.md', 'r') as f:
    readme = f.read()
    readme = re.sub('topogar', github_name, readme)

with open('README.md', 'w') as f:
    f.write(readme)
