value = input("고향을 입력하세요")
print(value + "사람이시군요")

age = input("나이를 입력하세요")
my_age = 40
if int(age) > my_age:
    print(str(age)+'살이시군요. 저보다 %s살 많네요'% str(int(age) - my_age))
# 여기서 elif를 쓸 때와 안 쓸 때의 차이를 눈여겨 보세요. 
elif int(age) <= my_age:
    print(str(age)+'살이시군요. 제가 %s살 많네요'% str(my_age - int(age)))
else:
    print("뭔가 값이 잘못 입력됐네요.")