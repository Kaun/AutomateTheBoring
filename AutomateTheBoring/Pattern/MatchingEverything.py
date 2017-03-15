import re
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo1 = nameRegex.search('First Name: Aleksey Last Name: Kaunnikov')
print(mo1.group(2))