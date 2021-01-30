# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_201814132_이헌수

from numpy import array                                         #numpy 의 array 기능 가져오기
from numpy import inner                                         #numpy 의 내적 기능 가져오기
from matplotlib import pyplot as plt                            

def vecprod(vec1, vec2):                                         #두 벡터의 내적 계산 함수
    result = inner(vec1,vec2)                                    #numpy 내장 내적 함수 
    return result                                                # 내적 계산 값 반환

print(vecprod(array([3,4,5,6]), array([1,2,3,4])))              #내적 할 두 함수 numpy.array 형식

def show_scatter(vec1, vec2):                                   #점으로 표현 할 두 벡터

    vec1 = array([1,2,3,4])                         
    vec2 = array([2,4,3,2])
    plt.scatter(vec1, vec2)                                     #점으로 표현할거야
    plt.show()                                                  #표 출력 
show_scatter([],[])                                             #함수 사용
