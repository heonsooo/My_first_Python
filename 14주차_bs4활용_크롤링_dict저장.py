from selenium import webdriver
import time
# from bs4 import BeautifulSoup

url = 'https://sites.google.com/view/kkbizintelligence/lecture'

def get_fame(url):
    driver = webdriver.PhantomJS('C:/Users/82103/Desktop/Python/연습파일들/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(url)
    time.sleep(1)
    
    course0 = []
    pjs = []
    result = {}

                                                                #수업 이름
    courses = driver.find_elements_by_tag_name('p')               # 모든 p태그 찾기 
    for course1 in courses:                                       # 찾은 p태그 를 텍스트처리
        course0.append(course1.text)       
    course = course0[9:14]                                        # p태그 중 hall of fame 과목만 새롭게 리스트처리

                                                                #프로젝트 팀원 리스트 
    projects = driver.find_elements_by_tag_name('small')        #모든 small 태그 찾기
    for ppp in projects:                                        #찾은 small 태그를 텍스트로
        pjs.append(ppp.text)                                    #학기- 팀명- 팀원 정보 리스트처리  
    pjs.pop()                                                   # hall of fame의 팀 아닌것 빼기 

    result[course[0]] = pjs[0:2]                              # 과목 : 프로젝트 dict처리
    result[course[1]] = pjs[2:7]
    result[course[2]] = pjs[8:11]
    result[course[3]] = pjs[12:14]
    result[course[4]] = pjs[-1]
    

    return result

print(get_fame(url))
