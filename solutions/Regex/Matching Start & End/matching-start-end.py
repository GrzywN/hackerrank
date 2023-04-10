Regex_Pattern = r"^\d\w\w\w\w\.$"

# \d - any digit
# \w - any word character
# The ^ symbol matches the position at the start of a string.
# The $ symbol matches the position at the end of a string.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
