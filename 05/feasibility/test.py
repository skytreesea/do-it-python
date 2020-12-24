#퍼센트 만들기 
percent = lambda x: str(round(x*100,2))+'%'
print(percent(0.011))
a = ['가','0.2233','23']
def percent_list(list_of_percent) : 
    new = [percent(float(i)) for  i in list_of_percent[1:]]
    new.insert(0,list_of_percent[0])
    return new
print(percent_list(a))

test = [[1,2,3],['구분',	'2022',	'2023']]
print(percent_list(test[1]))

number = 1
data = [float(i) for i in test[number][1:]]
print(data)