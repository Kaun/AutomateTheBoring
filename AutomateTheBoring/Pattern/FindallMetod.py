import re
#r'\(\d\d\d(\-| )?\d\d\)( )?\d(\-)?\d\d(\-)?\d\d'
match = re.compile(r'(8|8 )?(\(\d{3,5}\))? ?(\d-\d\d-\d\d)')
find = match.findall('My job phone:8(351)5-55-45 or 8 (351) 5-50-49')
print(find)