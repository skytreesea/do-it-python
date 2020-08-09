import re, usecsv, os	## 사용할 모듈을 임포트 합니다

English = 'She is a vegetarian. She does not eat meat. She thinks that animals should not be killed. It is hard for her to hang out with people. Many people like to eat meat. She told his parents not to have meat. They laughed at her. She realized they couldn\'t give up meat.'
## 영문을 English 객체에 저장합니다 
Korean = '그녀는 채식주의자입니다. 그녀는 고기를 먹지 않습니다. 그녀는 동물을 죽이지 말아야한다고 생각합니다. 그녀가 사람들과 어울리는 것은 어렵습니다. 많은 사람들이 고기를 좋아합니다. 그녀는 부모에게 고기를 먹지 말라고 말했습니다. 그들은 그녀를 비웃었다. 그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다. '
## 영문을 구글 번역기로 번역해 Korean 객체에 저장합니다 

os.chdir(r'J:\one-drive 20200728\MyScript\python\final_git_hub')
## CSV 파일을 저장하고 싶은 폴더로 이동합니다 

Korean_list = re.split('\.', Korean)
## split() 함수로 한글 문장을 나눠서 Korean_list에 저장합니다 
English_list = re.split('\.',English)
## 영문도 마침표를 기준으로 나눠서 English_list에 저장합니다
print(Korean_list)
## 중간 점검으로 Korean_list를 출력해 봅니다

total = []
## csv형 자료를 저장할 빈 리스트를 하나 만듭니다
for i in range(len(English_list)):
## for 문을 English_list 객체에 들어 있는 문장 수만큼 반복합니다
	total.append([English_list[i], Korean_list[i]]	)
## 첫 번째 열에 영어 문장, 두 번째 열에 한국어 문장이 들어 있는 리스트를 total에 추가합니다
usecsv.writecsv('Korean_English.csv', total)
