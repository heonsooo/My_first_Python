import csv
from bs4 import BeautifulSoup

def find_all_inventor(filename):                                                          #모든 발명인 이름 출력
    with open(filename , 'r' , encoding='utf-8') as f:
            xml_read = f.read()

    soup = BeautifulSoup(xml_read , 'lxml')
    one_invent = soup.find_all('soapenv:body')                                            #각 특허별로 리스트 만들기

    for inventor in one_invent :
        inv1 = inventor.find("ax2102:inventorinfoarray")
        inv_name1 = inv1.find_all('ax2102:name')
        inv_name0 = []

        for inv_name2 in inv_name1 : 
            inv_name0.append(inv_name2.text)

        print(inv_name0)
    return inv_name0

def find_all_inventor_eng(filename):                                                          #모든 발명인 영어 이름 출력
    with open(filename , 'r' , encoding='utf-8') as f:
            xml_read = f.read()
    soup = BeautifulSoup(xml_read , 'lxml')
    one_invent = soup.find_all('soapenv:body')                                                #각 특허별로 리스트 만들기


    for inventor in one_invent :
        inv1 = inventor.find("ax2102:inventorinfoarray")
        inv_name1 = inv1.find_all('ax2102:engname')
        inv_name0 = []

        for inv_name2 in inv_name1 : 
            inv_name0.append(inv_name2.text)

        print(inv_name0)
    return inv_name0

def find_inventor(filename,name):                                                         #발명인 이름 입력받고 특허, 초록 출력
        
    with open(filename , 'r' , encoding='utf-8') as f:                                    #파일 읽고 utf-8로 인코딩 후 f라는 변수로 취급 
        xml_read = f.read()

    soup = BeautifulSoup(xml_read , 'lxml')                                               #변환한 파일을 xml취급
    one_invent = soup.find_all('soapenv:body')                                            #각 특허별로 리스트 만들기
    co = 0 
    inv = []
    describ = []                                                                                                 
    for inventor in one_invent :                                                          
        inv1 = inventor.find("ax2102:inventorinfoarray")
        inv_name1 = inv1.find_all('ax2102:name')
        inv_name0 = []

        for inv_name2 in inv_name1 : 
            inv_name0.append(inv_name2.text)

            if name in inv_name0 :
                inventiontitle = inventor.find('ax2102:inventiontitle')
                inv_describ = inventor.find('ax2102:astrtcont')
                describ.append(inv_describ.text)
                inv.append(inventiontitle.text)

                co += 1
                break

    if co == 0 :
        print('이름을 확인해주세요')
    else: 
        print('%s 님이 발명한 특허 개수는 %d개 입니다.'  %(name , co))
        print('특허는 : ' ,inv, '입니다.')
        print('특허의 초록은' ,describ,'입니다.')

    with open(' 발명인 - 특허명.csv' , 'w', newline = '' , encoding='utf-8') as file :                         #csv 파일 쓰기 
        writer = csv.writer(file)
        writer.writerow(['발명인 입력하여 특허명, 초록을 저장 한 파일입니다.'])
        writer.writerow(['이름', '특허명', '초록'])
        for inv1 in inv:
            writer.writerow([name, inv1,describ[0]])
            describ.pop(0)
    return name, co, inv

def find_inventor_eng(filename,name):                                                     #발명인 영어 이름 입력받고 특허, 초록 출력
    
    with open(filename , 'r' , encoding='utf-8') as f:
        xml_read = f.read()

    soup = BeautifulSoup(xml_read , 'lxml')
    one_invent = soup.find_all('soapenv:body')                                             #각 특허별로 리스트 만들기
    co = 0 
    inv = []
    describ = [] 
    name1 = name.upper()                                                                                                
    for inventor in one_invent :
        inv1 = inventor.find("ax2102:inventorinfoarray")
        inv_name1 = inv1.find_all('ax2102:engname')
        inv_name5 = []

        for inv_name2 in inv_name1 : 
            k = inv_name2.text
            k = k.upper()
            inv_name5.append(k)

            if name1 in inv_name5 :
                inventiontitle = inventor.find('ax2102:inventiontitleeng')
                inv_describ = inventor.find('ax2102:astrtcont')
                describ.append(inv_describ.text)
                inv.append(inventiontitle.text)

                co += 1
                break


    if co == 0 :
        print('이름을 확인해 주세요')
    else: 
        print('%s 님이 발명한 특허 개수는 %d개 입니다.'  %(name , co))
        print('특허는 : ' ,inv, '입니다.')
        print('특허의 초록은' ,describ,'입니다.')

    with open(' 발명인(eng) - 특허명(eng).csv' , 'w', newline = '' , encoding='utf-8') as file : #csv 파일 쓰기 
        writer = csv.writer(file)
        writer.writerow(['Inventor , Invention Title, astrtcont In this csv file.'])
        writer.writerow(['Name', 'Invention Title-Eng', 'Astrtcont'])
        for inv1 in inv:
            writer.writerow([name, inv1,describ[0]])
            describ.pop(0)
    return name, co, inv
