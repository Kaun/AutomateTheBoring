import re

str = 'dsfapisdf pao(35191) 5-6588sjdf f[aoishf 5-50-49'
match = re.compile(r'(\(?\d\d\d\d\d\)?)? \d-\d\d-\d\d')
telsearch = match.search(str)
telnumber = telsearch.group()
print(telnumber)
