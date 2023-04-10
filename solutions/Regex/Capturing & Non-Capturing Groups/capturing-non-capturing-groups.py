Regex_Pattern = r'(ok){3,}'

# Parenthesis ( ) around a regular expression can group that part of regex together. This allows us to apply different quantifiers to that group.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
