Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'

# w+ : It will match the character w 1 or more times.
# [xyz]+ : It will match the character x, y or z 1 or more times.
# \d+ : It will match any digit 1 or more times.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
