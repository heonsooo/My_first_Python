import csv

def get_high(fn):                                                       # 전국 학교 중 사립 고등학교 찾는 함수
    data = []
    isfirst = True
    with open(fn, 'r', encoding='utf-8') as file:                      #utf-8 로 파일 열기
        csv_data = csv.reader(file)
        
        for nationwide_schools in csv_data:                             #csv 파일에 있는 정보를 list of list로 만들기 
            ns = nationwide_schools
            if isfirst :
                data.append(ns)
                isfirst = False
                                
            else:
                group_private =ns[4].strip()                          #학교분류 공립/사립 
                group_highschool =ns[2].strip()                       #초,중,고 분류
                if group_private== '사립' and group_highschool == '고등학교':  
                    data.append(ns)                                #사립 이면서, 고등학교의 행만 리스트에 추가
                    
        print(data)
                    
        data_school = []                                            #사립 고등학교를 넣을 리스트 생성
        for school in data:    
            data_school.append(school[1])                           #사립 고등학교 이름만 리스트에 추가
            data_school.sort()
        
        
        with open('week13_이헌수.csv' , 'w', newline = '' , encoding='utf-8') as file :                         #csv 파일 쓰기 
            writer = csv.writer(file)
            for ns in data_school: 
                ns = [ns]
                writer.writerow(ns)
    print(data_school)
    return data_school
    

get_high('w12_school.csv')
