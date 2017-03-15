import re
greedyRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyRegex.search('HaHaHaHaHaHa')
print(mo1.group())


nongreedyRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyRegex.search('HaHaHaHaHaHa')
print(mo2.group())
