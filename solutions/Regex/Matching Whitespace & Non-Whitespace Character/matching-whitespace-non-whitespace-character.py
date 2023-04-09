Regex_Pattern = r"\S\S\s\S\S\s\S\S"

# \s matches any whitespace character [ \r\n\t\f ].
# \S matches any non-white space character.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
