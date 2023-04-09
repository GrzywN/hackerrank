Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"

# \w matches any word character.
# \W matches any non-word character.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
