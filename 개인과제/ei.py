
import csv
from bs4 import BeautifulSoup

# 번호, 특허 명, 출원인, 발명가, 특허 초록, 특허 설명 


def write_Invent(filename):                                                                        
        
    with open(filename , 'r' , encoding='utf-8') as f:
        xml_read = f.read()

    soup = BeautifulSoup(xml_read , 'lxml')
    one_invent = soup.find_all('soapenv:body')                                                         
    co = 0 

    total_info = []
    
    for info in one_invent :                                #하나의 특허에서 정보 뽑기

        co += 1                                             #특허 하나 있을때마다 하나씩 추가 (특허개수 세는 용도)
        
        title = info.find('ax2102:inventiontitle')          #특허명 할당
        title = title.text                                  #특허명 text 

        apl1 = info.find('ax2102:applicantinfo')            #출원정보(부모 태그)
        apl2 = apl1.find_all('ax2102:name')                 #출원인 이름 할당
        apl3 = []                                           #출원인 이름 할당하고 text화 하기 위한 리스트 선언

        inv1 = info.find("ax2102:inventorinfoarray")        #발명정보(부모 태그)
        inv2 = inv1.find_all('ax2102:name')                 #발명인 이름 할당
        inv3 = []                                           #발명인 이름 할당하고 text화 하기 위한 리스트 선언

        des = info.find('ax2102:astrtcont')                 #특허의 초록 할당
        des = des.text                                      #특허의 초록 text 

        cla = info.find_all('ax2102:claim')                 #특허의 설명 할당
        claim = []                                          #특허의 설명 할당하고 text화 하기 위한 리스트 선언

        
        for apl4 in apl2 :                                  #출원인 이름 하나씩 뽑아가며 text화하고 위에서 선언한 리스트에 저장
            apl3.append(apl4.text)
        for inv4 in inv2 :                                  #발명인 이름 하나씩 뽑아가며 text화하고 위에서 선언한 리스트에 저장
            inv3.append(inv4.text)
        for cla1 in cla :                                   #특허 설명 하나씩 뽑아가며 text화하고 위에서 선언한 리스트에 저장
            claim.append(cla1.text)
        
   
        sub_info = []                                      #하나의 특허의 특허명, 출원인, 발명인, 초록, 설명 을 하나의 리스트로 만들 리스트 선언   
        sub_info.append(co)                                #특허 번호(개수 이지만 0부터 시작했으므로 번호로 가능) 리스트에 추가
        sub_info.append(title)                             #특허 명 리스트에 추가
        sub_info.append(apl3)                              #출원인 리스트에 추가
        sub_info.append(inv3)                              #발명가 리스트에 추가
        sub_info.append(des)                               #특허의 초록 리스트에 추가
        sub_info.append(claim)                             #특허 설명 리스트에 추가
        
        total_info.append(sub_info)
    print(total_info)                                      #본 데이터 내의 특허의 특허명, 출원인, 발명인, 초록, 설명 을 하나의 리스트로한 list of list 출력
                              
    
    with open(' 특허 정보 정리.csv' , 'w', newline = '' , encoding='utf-8') as file :               #csv 파일 쓰기
        writer = csv.writer(file)                                                                   
        writer.writerow(['특허 정리 파일입니다.'])                                            #csv파일 맨 상단에 소개 
        writer.writerow(['순서 번호, 특허 명, 출원인, 발명가, 특허 초록, 특허 설명'])                  #csv파일의 열 별 설명

        try : 
            
            for i in range(0,5000):
                if i != co:
                    writer.writerow([total_info[i][0], total_info[i][1], total_info[i][2],total_info[i][3], total_info[i][4], total_info[i][5]])    #i가 증가하면서 순서대로 저장

        except Exception: 
                writer.writerow(['%s개의 특허 정보 생성 완료.' %co])




    return co, title, apl4, inv4, des, claim
