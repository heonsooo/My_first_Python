from numpy import  array 
from numpy import matmul as mm

def matmul(input1, input2):                                                             #입력받은 행렬의 행렬 곱 함수
    if len(input1) and len(input2) and len(input1[0]) and len(input2[0]) == 2:          # 2x2 행렬이 맞는지 판단                                  
        mat_ver = [[cul for cul in v] for v in zip(*input2)]                             
    
        result = [[input1[n][0]*mat_ver[0][0] + input1[n][1]*mat_ver[0][1] , input1[n][0]*mat_ver[1][0] + input1[n][1]*mat_ver[1][1]] for n in [0,1]   ]    #8주차 과제에서 만든 2x2행렬 곱 함수 code 

        print('2x2 두 행렬의 곱은 ', result ,'입니다.')                                                                  #8주차에서 만든 함수로 구한 2x2 두 행렬의 곱셈 값

    else:
        print('2x2행렬의 곱이 아닙니다.')


        try : 
            result = mm(input1,input2)                                                      #행렬 곱
            print('두 행렬의 곱은 ' , '\n', result ,'입니다.')                                #결과 출력

        except Exception:                                                                   #결과 안나오는 예외 경우
            print('MatrixValueError')
            print('곱하려는 두 행렬의 형식을 확인 후 다시 시도해주세요.')

        else :
            return result                                                                   #두 행렬의 곱 값 반환



print('첫 번째 행렬을 만들어주세요 ')                       

try :
    A1 = list(map(int, input('행과 열의 개수를 입력하세요. (if 2 2 = 2x2행렬 ) : ').split()))                                                   #행렬의 크기 설정 2 2 -> 2x2 행렬 , 3 4 -> 3x4 행렬
    A2 = list(map(int, input('입력하신 행과 열에 맞게 행렬의 값을 입력하세요. (if 1 1 2 2 = [[1,1] ,[2,2]]) : ').split()))                        #행렬의 크기에 맞는 값 선언 3 2 1 3 ->[ [3,2], [1,3] ]
    a = array(A2).reshape(A1)                                                                                                                #첫 번째 행렬 a 생성
    
except Exception as e :
    print('에러 type :', type(e) )                                                                                                          #에러 발생 시, 에러 타입 확인 
    print('Error의 이유는', e,'입니다.', '\n', '확인 후 다시 입력해 주세요.')                                                                   # 에러의 이유 출력
    

else :
    print('첫번째 행렬' ,'\n', a)                                                                                                           # 위에서 행렬이 만들어 진다면, 만들어진 행렬 출력 
    print('두 번째 행렬을 만들어 주세요')                                                                                                    # 첫 번째 행렬이 만들어지면, 두 번째 행렬 만들기 

    try :
        B1 = list(map(int, input('행과 열의 개수를 입력하세요. (if 2 2 = 2x2 ) : ').split()))
        B2 = list(map(int, input('입력하신 행과열에 맞게 행렬의 값을 입력하세요. (if 1 1 2 2 = [[1,1] ,[2,2]]) : ').split()))
        b = array(B2).reshape(B1)
    
    except Exception as e :
        print('에러 type :', type(e) )
        print('Error의 이유는', e,'입니다.', '\n', '확인 후 다시 입력해 주세요.') 
    
    else:   
        print('두 번째 행렬' ,'\n', b)
        matmul(a, b)                                                                                                                        #만들어진 두 행렬의 곱 실행
        