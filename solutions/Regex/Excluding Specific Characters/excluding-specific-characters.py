Regex_Pattern = r'^[^\d][^aeiou][^bcDF]\S[^AEIOU][^\.,]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
