Regex_Pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10'

# This tool (\1 references the first capturing group) matches the same text as previously matched by the capturing group.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
