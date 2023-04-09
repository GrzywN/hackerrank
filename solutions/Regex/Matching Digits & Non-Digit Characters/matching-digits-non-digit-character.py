Regex_Pattern = r"^..\D..\D...."

# ^abc$    start (^) / end ($) of the string
# . any character except the new line
# \D any character that is not a digit

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
