Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'

# w* : It will match the character w 0 or more times.
# [xyz]* : It will match the characters x, y or z or 0 more times.
# \d* : It will match any digit 0 or more times.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
