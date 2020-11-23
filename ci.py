
from bs4 import BeautifulSoup
import re
import csv

def find_key_title(filename):

    with open(filename , 'r' , encoding='utf-8') as f:                                                        #text 파일을 불러와서 xml로 읽음
        xml_read = f.read()     
    soup = BeautifulSoup(xml_read , 'lxml')
    co = 0                                                                                                    #특허 개수 세기
    data_key_title = []                                                                                       #키워드 포함 된 특허 제목 리스트
    regex_eng = '[a-zA-Z0-9_]'                                                                                #영어 문자열
    lan_eng = re.compile(regex_eng)
    regex_kor = '[^a-zA-Z_]'                                                                                  #영어 제외 문자열
    lan_kor = re.compile(regex_kor)

    print('찾고자 하는 특허 키워드의 언어를 선택해주세요' )
    lan = input( '어떤 언어로 입력하시겠습니까? (\'한글\' 또는 \'영어\'로 입력해주세요) :' )

    if lan == '한글' :
        keyword = input('특허 키워드 입력: ')                                                                  #입력 키워드 
        title_tag = soup.find_all('ax2102:inventiontitle')                                                    #모든 특허의 특허 명 리스트화
        for title in title_tag:                                                                               #특허 제목 리스트에서 하나씩 키워드 포함 여부 탐색
            if keyword in title.text:
                t = title.text
                co += 1
                data_key_title.append(t)
            
        if co >= 1:
            print('\'%s\'단어가 포함 된 특허는 총 %d개 입니다.' '\n' %(keyword, co))
            print(data_key_title)
            with open(' 특정단어 - 특허명.csv' , 'w', newline = '' , encoding='utf-8') as file :                #csv 파일 쓰기 
                writer = csv.writer(file)
                writer.writerow(['특정 단어가 포함된 특허 이름을 저장 한 파일입니다.'])                            #파일 첫 행에 파일 소개
                writer.writerow(['특정단어', '특허명'])                                                         #파일 두번째 행에 열 분류
                for title in data_key_title:
                    writer.writerow([keyword, title])                                                          #키워드 , 특허제목  하나에 한 행씩 작성
        elif co == 0:
            lan_kor2 = len(lan_kor.findall(keyword))

            if lan_kor2+1 <= len(keyword):
                print('입력하신 특허 키워드에 영어가 포함되어 있습니다. 확인해주세요.')
            else :
                print('\'%s\'단어를 포함하는 특허가 없습니다.' %keyword )


    elif lan == '영어' :
        title_eng_tag = soup.find_all('ax2102:inventiontitleeng')
        keyword_eng = input('특허 키워드(영어) 입력 :')
        for title in title_eng_tag:
            if keyword_eng in title.text:
                t = title.text
                co += 1
                data_key_title.append(t)

        if co >= 1:
            print('\'%s\'단어가 포함 된 특허는 총 %d개 입니다.' '\n' %(keyword_eng, co))
            print(data_key_title)
            with open(' 특정단어(Eng) - 특허명(Eng).csv' , 'w', newline = '' , encoding='utf-8') as file :            #csv 파일 쓰기 
                writer = csv.writer(file)   
                writer.writerow(['특정 단어가 포함된 특허 이름을 저장 한 파일입니다.'])                                 #파일 첫 행에 파일 소개
                writer.writerow(['Appointed Words', 'Invention Title - Eng'])                                       #파일 두번째 행에 열 분류
                for title in data_key_title:
                    writer.writerow([keyword_eng, title])                                                           # 키워드 , 특허제목  하나에 한 행씩 작성
        elif co == 0:

            lan_eng1 = len(lan_eng.findall(keyword_eng))
            
            if lan_eng1 +1 <= len(keyword_eng) :
                print('입력하신 특허 키워드에 한글이 포함되어 있습니다. 확인해주세요.')
            else : 
                print('\'%s\'단어를 포함하는 특허가 없습니다.' %keyword_eng )

    else:
        print('원하는 언어를 확인 후 다시 실행해주세요.')
    return data_key_title