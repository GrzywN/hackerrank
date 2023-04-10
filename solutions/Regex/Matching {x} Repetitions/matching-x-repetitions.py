Regex_Pattern = r'^([a-z]|[A-Z]|[02468]){40}([13579]|\s){5}$'

# w{3} : It will match the character w exactly times.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
