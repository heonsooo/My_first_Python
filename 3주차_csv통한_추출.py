f = open('week3.csv','r')
info = f.readlines()
f.close()

Female_all, Male_all = 0.0, 0.0
count_F , count_M = 0, 0
grade_all_16, grade_all_17, grade_all_18 = 0.0, 0.0, 0.0
count_16, count_17, count_18 = 0, 0, 0
Nope = 0


for line in info :
    line = line.strip().split(',')

    if 'F' in str(line[2]) :
        Female = line[3]
        Female = float(Female)
        Female_all += Female
        count_F += 1

    elif 'M' in str(line[2]) :
        Male = line[3]
        Male = float(Male)
        Male_all += Male
        count_M += 1

    elif not  'F' in str(line[2]) and not 'M' in str(line[2]) :
        Nope += 1

    else :
       break

for line in info :
    line = line.strip().split(',')
    if '2016' in str(line[0]) :
        grade_16 = line[3]
        grade_16 = float(grade_16)
        grade_all_16 += grade_16
        count_16 += 1
       
    elif '2017' in str(line[0]) : 
        grade_17 = line[3]
        grade_17 = float(grade_17)
        grade_all_17 += grade_17
        count_17 += 1
     
    elif '2018' in str(line[0]):
        grade_18 = line[3]
        grade_18 = float(grade_18)
        grade_all_18 += grade_18
        count_18 += 1
        
    elif not '2016' in str(line[0]) and not '2017' in str(line[0]) and not '2018' in str(line[0]) :
        Nope += 1

    else : 
        break   


Female_ave = float(Female_all / count_F)
Male_ave = float(Male_all / count_M)
print('전체 평균 : %5.3f' %round((Female_ave + Male_ave)/2, 3) )
print('여자 평균 : %5.3f' %round(Female_ave, 3))
print('남자 평균 : %5.3f' %round(Male_ave, 3))

grade_ave_16 = float(grade_all_16 / count_16)
grade_ave_17 = float(grade_all_17 / count_17)
grade_ave_18 = float(grade_all_18 / count_18)
print('16학번 평균 : %5.3f' %round(grade_ave_16, 3))
print('17학번 평균 : %5.3f' %round(grade_ave_17, 3))
print('18학번 평균 : %5.3f' %round(grade_ave_18, 3)) 