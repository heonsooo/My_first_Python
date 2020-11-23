def addall(num_list):                           #리스트 합을 반환하는 함수 
    
    if len(num_list) >= 1 :

        sum_num_list = sum(num_list) 

    elif len(num_list) == 0 : 
        sum_num_list = 0

    return sum_num_list


def bigger(a, b):                            #두 값중 더 큰값을 반환하는 함수
    if a >= b :
       result = a
    elif b >= a :
        result = b
    elif a == b :
        print('서로 다른 두 수를 입력하세요.')
    return result

def rep(string, char):                      #특정 단어를 제거해주는 함수 
    if char in string :
        result = string.replace(char, '')
    
    return result

def sigma(n):                               # 1부터 n까지 더한 값을 반환하는 함수
    if n != 0 :
        return n + sigma(n-1)
    else:
        return 0

def facto(n):                                # n!을 반환하는 함수 
    if n != 0 :
        return n*facto(n-1)
    else :
        return 1

x1 = addall([80, 70, 60])      
x2 = addall([])
print(x1)
print(x2)

x1 = bigger(10.0, 50.0)
x2 = bigger(-3, 7)
print(x1)
print(x2)

res = rep('I love you', 'o')
print(res)

num = input('1부터 n까지 합을 원하는 임의의 정수를 입력하세요 : ' )
num = int(num)
print(sigma(num))

n = input('n! 의 값을 원하는 임의의 정수를 입력하세요 : ' )
n = int(n)
print(facto(n))
