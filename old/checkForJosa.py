def checkForJosa(c):
	# 받침이 있으며 True를 받침이 없으면 False를 반환합니다. 
    return (int((ord(c) - 0xAC00) % 28) != 0)
	
#예제: 
sample_list= ['가' ,'나' ,'받', '공' ,'삼', '리'] 
for i in sample_list:
	if checkForJosa(i):
		print("%s은 받침이 있습니다" % i )
	elif checkForJosa(i) is not True :
		print("%s는 받침이 없습니다" % i )		 
		
