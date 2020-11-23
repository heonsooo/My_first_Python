import csv
from bs4 import BeautifulSoup

def find_titles(filename,name):
    with open(filename , 'r' , encoding='utf-8') as f:
        xml_read = f.read()

    soup = BeautifulSoup(xml_read , 'lxml')
    one_invent = soup.find_all('soapenv:body')

    for one in one_invent:
        title_1 = one.find('ax2102:inventiontitle')
        print(title_1.text)
        
    return title_1.text

def find_claims(filename,name):
    with open(filename , 'r' , encoding='utf-8') as f:
        xml_read = f.read()

    soup = BeautifulSoup(xml_read , 'lxml')
    one_invent = soup.find_all('soapenv:body')
    cl = []
    inv_title_real = []

    for invent in one_invent :                                                      #특허 하나하나 탐색하기

        inv_title0 = []
        inv_title = invent.find('ax2102:inventiontitle')
        inv_title0.append(inv_title.text)
        
        if name in inv_title0:
            inv_title_real.append(inv_title.text) 
            claim = invent.find_all('ax2102:claim')
            claim2 = []
            for claim1 in claim:
                claim2.append(claim1.text)
            cl.append(claim2)

    if len(inv_title_real) >= 1:
            
        print(inv_title_real)
        print(cl)   
        with open('특허명 - 특허 설명.csv', 'w',newline= '' , encoding='utf-8') as file :
            writer = csv.writer(file)
            writer.writerow(['특정 특허에 대한 특허 설명 파일입니다.'])
            writer.writerow(['특허명', 'Claims'])
            for nn in cl :
                writer.writerow([name, nn])
    else :
        print('특허명을 확인해주세요.')        

    return inv_title_real, cl

