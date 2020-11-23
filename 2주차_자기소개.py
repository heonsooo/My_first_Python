Hello = ['입니다.', '잘부탁드립니다.']
pack = ['안녕하세요', '저는', '산업공학과로', '이헌수' ]


age = 5**2

Introduce0 = '나이는'
Introduce1 = age 
Introduce2 = '살'
Introduce3 = '저의 취미는 운동입니다.'
Introduce4 = '헬스를 자주 하며,'
Introduce5 = '축구를 매우 좋아합니다.'

goal1 = '본 과목에서 저의 첫 번째 목표는 A+ 이고, ' 
goal2 = '두 번째 목표는 제가 원하는 값을 출력하는 것입니다.'
goals =[goal1, goal2]


Hello.append(Introduce0)
Hello.append(Introduce1)
Hello.append(Introduce2)
Hello.append(Introduce3)
Hello.append(Introduce4)
Hello.append(Introduce5)
Hello.extend(goals)
del Hello[1]

a, b, c, d, e = pack

Bye = '앞으로의 수업에서' + ' ' + '좋은 모습 보여드리도록 성실하게 공부하겠습니다.'
Thank = '감사합니다.'

print('이름 : {} \n나이 : {}살 \n자기소개 : {} {} {} {} {} {} {} {} \n {} {} {} \n {} {} \n {} \n {} ' 
       .format(e, age, a, b, c, d, Hello[2], Hello[3], e, Hello[0],
        Hello[4], Hello[5], Hello[6], Hello[7], Hello[8], Bye, Thank   ))