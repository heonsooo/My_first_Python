import json

def cut_if(result,x,y):                                                #title에 python 이 있는지 없는지 확인 후 분류하는 함수
    print(result)                                                      #title 값 출력
    if 'Python' in result or 'python' in result:                       #title 에 python이 있으면, title(in python) 리스트에 추가 
       x.append([result])                                                       
    else :
        y.append([result])                                             #title 에 python이 없으면, title(not in python) 리스트에 추가 
    return x, y
#input = 'w15_python.json'
def get_count(input):
    with open(input, 'r', encoding='utf-8') as f:                      # json 파일 열기
        w15_str = f.read()
        w15_data = json.loads(w15_str)

    p = []                                                              #title(in python)  리스트 
    q = []                                                              #title(not in python)  리스트
                                                               
    try :
        for i in range(0,50):                                           
            result = w15_data['data']['children'][i]['data']['title']
            cut_if(result,p,q)

    except Exception :                                                                              
        
        result2 = w15_data['data']['children'][13]['data']["secure_media"]["oembed"]['title']       
        cut_if(result2,p,q)
        
        result3 = w15_data['data']['children'][13]['data']["media"]["oembed"]["title"]
        cut_if(result3,p,q)
        
        result4 = w15_data['data']['children'][i-1]['data']["secure_media"]["oembed"]["title"]
        cut_if(result4,p,q)

        result5 = w15_data['data']['children'][i-1]['data']["media"]["oembed"]["title"]
        cut_if(result5,p,q)

        print('끝났습니다.')

    #각 title 개수
    print('Total Title count : %d' % (len(p) + len(q)))


    
    print('title(in python) count: %d' %len(p))

    return len(p), len(q) 

get_count(input('json파일의 경로를 입력해주세요.:') )

# C:/Users/82103/Desktop/Python/연습파일들/w15_python.json  
