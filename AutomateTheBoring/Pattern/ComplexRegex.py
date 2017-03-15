import re
phoneRegex = re.compile(r'''(
    (\d{3})|(\d{3}\))?      #area cod
    (\s|-|\.)?              #separator
    \d{3}                   #first three digits
    (\s|-|\.)               #separator
    \d{4}                   #last 4 digits
    )''', re.VERBOSE)