import re
pattern = re.compile('this')
string = 'search inside of this text please!'

print(pattern.search(string))
