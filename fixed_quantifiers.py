import re

pattern = "\.{3,}"

txt = 'Hello!... Wait. How goes?..... GoodBye!..'

print(re.findall(pattern, txt))
