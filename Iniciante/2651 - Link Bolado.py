import re

valores = input()

if re.search('zelda', valores, re.IGNORECASE):
    print('Link Bolado')
else:
    print('Link Tranquilo')
