import re
mach = re.compile(r'Bat(wo)+man')
search = mach.search('Batman faind Batwowowoman')
print(search.group())

machHa = re.compile(r'(Ha){3,5}?')
searchHa = machHa.search('HaHaHaHaHaHa')
print(searchHa.group())

atReg = re.compile(r'.at')
seachAt = atReg.findall('what seachat')
print(seachAt)