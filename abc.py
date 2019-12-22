import re
text = '나의 이메일 아이디는 life@naver.com입니다. 당신의 아이디는  live@naver.com'
print(re.findall('[a-z]+\@[a-z]+\.[a-z]+', text))
    
     