class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
   
    def get_status(self) :
        print('제 이름은 %s입니다. 직업은 %s이고, 나이는 %d살 입니다. ' %(self.name, self.job , self.age))
    
class Student(Person):
    def __init__(self, major, std_num, grade, GPA, my_prof ) :
        self.major = major
        self.std_num = std_num    
        self.grade = grade
        self.GPA = GPA
        self.my_prof = my_prof
    
    def set_prof(self, Name):
        self.my_prof = Name
    
    def __str__(self) :
        return ('학번은 %d이고 %d학년 입니다.전공은 %s이고, 성적은 %.1f 입니다. 저의 지도교수님은 %s이십니다.  ' %(self.std_num , self.grade , self.major, self.GPA , self.my_prof ))


per1 = Person('이헌수', 25 , '대학생')
per1.get_status()
stu1 =Student('산업공학과',201814132, 3, 4.5, 'Yoon' )

'''
per2 = Person('김철수', 25 , 'konkuk\'s doll ')
per3 = Person('길동쓰', 25 , 'konkuk\'s man ')

stu2 =Student('산업공학과',201714132, 4, 3.5, 'Yoon' )
stu3 =Student('산업공학과',201914132, 2, 2.5, 'Yoon' )

per2.get_status()
per3.get_status()
stu1.set_prof('Soo')
stu2.set_prof('Kim')
print(stu1 , '\n' , stu2 , '\n' , stu3)
'''