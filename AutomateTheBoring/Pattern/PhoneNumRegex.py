import re
str = '(495) 5-50-49 5-55-55'
match = re.compile(r"(\(\d{3}\))? (\d-\d\d-\d\d)")

phone = match.findall(str)
print(phone)
# phone = match.search(str)
# area, numberPhone = phone.groups()
# print(area)
# print(numberPhone)