Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$'
# Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.([a-z]|[A-Z])+$'

# (Bob|Kevin|Stuart) will match either Bob or Kevin or Stuart.
# ([a-f]|[A-F]) will match any of the following characters: a, b, c, d, e, f, A, B, C, D, E, or F.


# https://stackoverflow.com/questions/34292024/regular-expression-vs-vs-none
# ^[a-zA-Z]+$ matches any alphabetic string (consisting of the letters a-z, large or small)
# of size 1 or longer. The ^ and $ characters mean "start" and "end" of the line, so they
# only match full lines consisting of one "word".


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
