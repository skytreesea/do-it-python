import re

pattern = re.compile("[가-힣\s]+[.?!]")
text = "안녕하세요! 반갑습니다. 저는 ChatGPT입니다. Hello, World!"
matches = pattern.findall(text)
print(matches)
