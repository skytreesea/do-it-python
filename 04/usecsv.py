import csv, os, re
# opencsv is a method, which can open csv-style files
# you can simply use it by putting the name of the file. 
# if you want to open "a.csv", then after "import usecsv"
# opencsv('a.csv') or a = opencsv('a.csv')  

def opencsv(filename):
    f=open(filename, 'r', encoding='utf8')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output
	
# writecsv is a method, which can change your csv-style list data into a new csv file 
# if you want to change a list, like a = [[1,2,3],[2,3,4]] into a csv file
# after import usecsv, then "writecsv('a.csv', a)

def writecsv(filename, the_list):
    with open(filename,'w',newline='', encoding='utf-8-sig') as f:
        a=csv.writer(f, delimiter=',')
        a.writerows(the_list)

# switch is a method, which can change the element that can be changed into figure style into float
# as you change a csv file into a csv style, all the elements are of string style
# if you want to change it into float or integer, you can use the method of switch.
# By changing them into the data of float, you can use it as figure. 
 
def switch(listName):
    for i in listName:        
        for j in i:
            try:
                i[i.index(j)] =float(j.replace(',', '')) 
            except:
                pass
    return listName