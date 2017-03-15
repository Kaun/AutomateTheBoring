import pprint
message = 'fs fwfd lkjp aaaa'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1
pprint.pprint(count)