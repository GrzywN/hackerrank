Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{,3}$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
