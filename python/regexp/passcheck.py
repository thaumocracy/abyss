import re

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")

password = 'Whatever@#$3'

check = pattern.fullmatch(password)


print(check)
