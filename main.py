import ai
import bi
import ci
import di
import ei
import csv
from bs4 import BeautifulSoup

print('특허 정보 검색프로그램을 실행합니다.')
fn = '개인과제data.txt'

print('원하시는 검색조건의 숫자를 입력하세요' , '\n', '1) 출원인 입력하여 특허찾기 2) 발명가 입력하여 특허찾기 3) 키워드 입력하여 특허찾기 4) 특정 특허의 특허 설명 5) 본 데이터내의 특허 정보 정리')

a = input('1 or 2 or 3 or 4 or 5 : ')

if a == '1' :
    print('출원인을 검색하여 특허 찾기를 선택하셨습니다.')
    language = input('출원인의 이름을 어떤 언어로 입력하시겠습니까? (\'한글\' 또는 \'영어\'로 입력해주세요) : ')

    if language == '한글' :
        print('출원인 - 한글이름으로 찾기를 선택하셨습니다. ')
        name = input('찾고자하는 출원인의 이름을 입력해주세요. (출원인 목록을 확인하려면 1번을 눌러주세요.) : ')
        print('잠시만 기다려 주세요..')
        try :
            if name == '1' :
                ai.find_all_applicant(fn)
                name = input('출원인의 이름을 입력해주세요. : ')
                print('잠시만 기다려 주세요..')
                ai.find_apllicant(fn,name)
            else:
                ai.find_apllicant(fn,name)
            
        except Exception :
            print('이름을 확인해 주세요!')

    elif language == '영어':
        name = input('Please typing English name that you want to find. (If you want check the list of applicants, input number 1) : ')
        print('Pleas waiting..')
        try :
            if name == '1' :
                ai.find_all_applicant_eng(fn)
                name = input('Please typing English name that you want to find. : ')
                ai.find_apllicant_eng(fn,name)
            else:
                ai.find_apllicant_eng(fn,name)
            
        except Exception :
            print('Please Check name! ')
    else :
        print('\'한글\' 또는 \'영어\'를 입력해주세요.')

        
elif a == '2' :
    print('\n','발명인을 검색하여 특허 찾기를 선택하셨습니다.')
    language = input('발명인의 이름을 어떤 언어로 입력하시겠습니까? (\'한글\' 또는 \'영어\'로 입력해주세요) : ')

    if language == '한글' :
        name = input('찾고자하는 발명인의 이름을 입력해주세요. (발명인의 목록을 확인하려면 1번을 눌러주세요.) :')

        if name == '1' :
            bi.find_all_inventor(fn)
            name = input('발명인의 이름을 입력해주세요. : ')
            print('로딩 중입니다..')
            bi.find_inventor(fn,name)
        else:
            print('로딩 중입니다..')
            bi.find_inventor(fn,name)

    elif language == '영어':
        name = input('Please typing English name that you want to find. (If you want check the list of Inventors, input number 1) : ')
        print('Pleas waiting..')
        try :
            if name == '1' :
                
                bi.find_all_inventor_eng(fn)
                name = input('Please typing English name that you want to find. : ')
                bi.find_inventor_eng(fn,name)
                
            else:
                bi.find_inventor_eng(fn,name)
        except Exception :
            print('Please Check name! ')
    else :
        print('\'한글\' 또는 \'영어\'를 입력해주세요.')

elif a == '3':
    print('키워드을 검색하여 특허 찾기를 선택하셨습니다.')
    print('로딩 중입니다..')    
    ci.find_key_title(fn)


elif a == '4':
    print('\n', '특정 특허의 특허 설명 찾기를 선택하셨습니다.')
    name = input('찾고자하는 특허명을 입력해주세요. (특허 목록을 출력하려면 \'특허-목록\'을 입력해주세요.): ')
    

    if name == '특허-목록':
        
        di.find_titles(fn,name)
        name = input('찾고자하는 특허명을 입력해주세요.:')
        print('로딩 중입니다.. ')
        di.find_claims(fn, name)

        
    else :
        print('로딩 중입니다..')
        di.find_claims(fn, name)
    
elif a == '5' :
    print('본 데이터 내의 특허 명, 출원인, 발명가, 특허 초록, 특허 설명을 출력 및 저장하는 프로그램입니다. ')
    print('로딩 중입니다..','\n')
    ei.write_Invent(fn)


else :
    print('입력 번호를 확인 후 다시 시도해주세요.')