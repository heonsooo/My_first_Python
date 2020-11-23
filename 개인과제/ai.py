
import csv
from bs4 import BeautifulSoup

def find_all_applicant(fn):                                           #출원인 이름 목록 출력
    with open(fn , 'r' , encoding='utf-8') as f:
            xml_read = f.read()
    soup = BeautifulSoup(xml_read , 'lxml')
    one_invent = soup.find_all('soapenv:body')                       #각 특허별로 리스트 만들기
    for apl in one_invent :
        apl1 = apl.find('ax2102:applicantinfo')                     #특허 출원 정보 태그 
        apl_name = apl1.find_all('ax2102:name')                     #특허 출원인 이름
        apl_name_list = []
        
        for apl_name_text in apl_name : 
            apl_name_list.append(apl_name_text.text)
            
        print(apl_name_list)

    return apl_name_list

def find_all_applicant_eng(fn):                                       #출원인 이름(영어)목록 출력
    with open(fn , 'r' , encoding='utf-8') as f:
            xml_read = f.read()
    soup = BeautifulSoup(xml_read , 'lxml')
    one_invent = soup.find_all('soapenv:body')                        #각 특허별로 리스트 만들기
    
    for apl in one_invent :
        apl1 = apl.find('ax2102:applicantinfo')                       #특허 출원 정보 태그
        apl_name1 = apl1.find_all('ax2102:engname')                   #특허 출원인 영어 이름
        apl_name0 = []
        
        for apl_name2 in apl_name1 : 
            apl_name0.append(apl_name2.text)
            
        print(apl_name0)

    return apl_name0

def find_apllicant(fn,name):                                          #출원인 이름 입력받고 특허 출력
    with open(fn , 'r' , encoding='utf-8') as f:
        xml_read = f.read()
   
    soup = BeautifulSoup(xml_read , 'lxml')
    one_invent = soup.find_all('soapenv:body')                         #각 특허별로 리스트 만들기
    co = 0 
    inv = []
    date = []
                                                                       
    for apl in one_invent :
        apl1 = apl.find("ax2102:applicantinfo")                         #특허 출원 정보 태그
        apl_name1 = apl1.find_all('ax2102:name')                         #특허 출원인 이름
        apl_name0 = []
        
        for apl_name2 in apl_name1 :                                   #출원인 이름 리스트에 추가
            apl_name0.append(apl_name2.text)
    
            if name in apl_name0 :                                     #리스트에 입력받은 이름값이 있는지 확인
                apl_inv = apl.find('ax2102:inventiontitle')            #존재하면, 이 특허의 이름 찾기
                apl_date = apl.find('ax2102:applicationdate')          #존재하면, 이 특허의 출원 날짜 찾기
                
                inv.append(apl_inv.text)                               #특허 이름 리스트에 추가
                date.append(apl_date.text)                             #특허 출원 날짜 리스트에 추가
                
                co += 1                                                #특허 개수 +1 해줌
                break

    if co == 0 :                                                       #입력 받은 사람의 출원정보가 없음
        print('이름을 확인해 주세요')                                   
    else: 
        print('\n %s 님이 출원한 특허 개수는 %d개 입니다.'  %(name , co))
        print('특허는 : ' ,inv, '입니다.')
        print('특허 출원 날짜는 ' ,date, '입니다.')

    with open(' 출원인 - 특허명.csv' , 'w', newline = '' , encoding='utf-8') as file :                         #csv 파일 쓰기 
        writer = csv.writer(file)
        writer.writerow(['출원인입력하여 특허명, 출원 날짜가 저장 된 파일입니다.'])             #파일 맨위에 파일 소개
        writer.writerow(['이름', '특허명', '출원 날짜'])                                     #csv 각 열 구분

        for inv1 in inv:
            writer.writerow([name, inv1, date[0]])                                          #이름, 특허 명, 출원 날짜 입력
            date.pop(0)                                                                     #날짜 앞에서부터 하나씩 삭제 (이중 for문을 사용불가하다고 판단하였습니다.) 
        
         
    
    return name, co, inv

def find_apllicant_eng(fn,name):                                      #출원인 영어 이름 입력받고 특허 출력
    with open(fn , 'r' , encoding='utf-8') as f:
        xml_read = f.read()

    soup = BeautifulSoup(xml_read , 'lxml')
    one_invent = soup.find_all('soapenv:body')                  #모든 특허 list of list로 저장                                                   
    co = 0 
    inv = []
    date = []
    name1 = name.upper()                                       #입력받은 이름 모두 대문자로 변환한 값 저장
                                                                                                          
    for apl in one_invent :                                    #특허 하나씩 뽑아서 검색        
        apl1 = apl.find("ax2102:applicantinfo")
        apl_name1 = apl1.find_all('ax2102:engname')

        apl_name5 = []
        
        for apl_name2 in apl_name1 : 
            k = apl_name2.text
            k = k.upper()                                       #특허 출원인 이름도 대문자로 변경하여 저장
            apl_name5.append(k)
         
            
            if name1 in apl_name5 :                             #입력받은 대문자 변환 이름 값과 파일 내의 출원인 대문자 변환 이름 값 있는지 확인
                apl_inv = apl.find('ax2102:inventiontitleeng')  #있으면, 영어 특허 명 찾기
                apl_date = apl.find('ax2102:applicationdate')   #있으면 출원 날짜 찾기
                inv.append(apl_inv.text)                        #영어 특허명 리스트에 추가
                date.append(apl_date.text)                      #출원날짜 리스트에 추가
                co += 1                                         #특허 1개 추가
                break

    if co == 0 :
        print('Please Check EngName ')
    else: 
        print('%s 님이 출원한 특허 개수는 %d개 입니다.'  %(name , co))
        print('특허는 : ' ,inv, '입니다.')
        print('특허 출원 날짜는 ' ,date, '입니다.')

    with open(' 출원인(eng) - 특허명(eng).csv' , 'w', newline = '' , encoding='utf-8') as file :                         #csv 파일 쓰기 
        writer = csv.writer(file)
        writer.writerow(['Applicant , Invention Title, Application Date In this csv file.'])
        writer.writerow(['Name', 'Invention Title - Eng ', 'Application Date'])

        for inv1 in inv:
            writer.writerow([name, inv1, date[0]])
            date.pop(0)

    return name, co, inv
