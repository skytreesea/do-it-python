import csv, os, re
# 아래 작은 따옴표 안에 경로를 추가해줍니다. 
os.chdir(r'###### 경로 추가 Add Path here ######')
def opencsv(filename):
    f=open(filename, 'r')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output

total = opencsv('pop_region.csv')
def crease(figure):
    if re.search('-',figure):
        return "감소"
    else: 
        return "증가"
start_year = total[0][1]
end_year = total[0][3]

with open('read_it.txt','w') as f:
    for i in total[2:]:
        creasing = crease(i[-2])
        f.write('\n%s의 %s년 인구는 %s명(%s)으로 %s년 %s명(%s)에 비하여 %s명 %s함, 점유율 변동(%s)' % (i[0], end_year, i[3],i[4],start_year,i[1],i[2],re.sub('-','',i[-2]), creasing, i[-1]))
