def calculator(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "숫자형 데이터만 입력 가능합니다."
    return a+b, a-b, a*b, a/b

print(calculator(10,2))
print(calculator(10,'사람'))
