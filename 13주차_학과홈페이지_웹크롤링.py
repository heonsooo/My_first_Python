import requests

from bs4 import BeautifulSoup
#https://www.konkuk.ac.kr/jsp/Coll/coll_01_04_05_01_tab01.jsp
url = input('원하는 학과의 소개 페이지 URL을 입력하세요 :')
def crawler(url):

    req = requests.get(url,verify=False)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    k = []
    mj= soup.select('div.contents_area > h1 > b')
    # print(mj)
    major= mj[0].text
    a = soup.select('tr')
    try :
        for n in range(1,30):
            b = a[n].text
            b = b.split('\n')
            b.pop(0)
            b.pop(0)
            b.pop(1)
            b.pop()
            k.append(b)
    except Exception :
        print(major, '%d분의 교수님 정보 출력' % len(k))

    return k

print(crawler(url))
