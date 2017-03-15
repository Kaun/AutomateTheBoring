import re
namesRegex = re.compile(r'Agent (\w)\w+', re.I)
text = namesRegex.sub(r'\1***', 'Agent Alice gave the secret documents to agent Bob')
print(text)