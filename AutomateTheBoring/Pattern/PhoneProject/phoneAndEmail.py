import  re
phoneRegex = re.compiler(r'''(
    \+?      #+
    (\d)?   #7 or 8
    \s?     #space
    (\d{3}|\d{5}|\(\d{3}\)|\(\d{5}\))?    #area cod
    )''')