import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('The many picturies in the flat'))