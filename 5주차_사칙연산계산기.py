in_put = input('계산하고자 하는 사칙연산을 입력하세요 (+, - , *, /) : ' )

num = ['.', '0','1','2','3', '4', '5', '6', '7','8', '9']
sym = ['+' , '-', '/', '*']

def mul(exp) :                             #곱셈 함수
    a = exp.find('*')                      #곱셈의 처음 위치
    
    if a == 1:
        result_mul1 = exp[a-1]
        exp_mul1 = exp[:a-1]

    elif a == 2:
        if exp[a-2] in num :
            result_mul1 = exp[a-2] + exp[a-1]
            exp_mul1 = exp[:a-2]
        elif exp[a-2] in sym :
            result_mul1 = exp[a-1]
            exp_mul1 = exp[:a-1]

    elif a >= 3:
        if exp[a-2] in sym :
            result_mul1 = exp[a-1]
            exp_mul1 = exp[:a-1]
        elif exp[a-2] in num :
            result_mul1 = exp[a-2] + exp[a-1]
            exp_mul1 = exp[:a-2]
            if exp[a-3] in num :
                result_mul1 = exp[a-3] + exp[a-2] + exp[a-1]
                exp_mul1 = exp[:a-3]
                if len(exp[0:a]) >= 4 :
                    if exp[a-4] in num :
                        result_mul1 = exp[a-4] + exp[a-3] + exp[a-2] + exp[a-1]
                        exp_mul1 = exp[:a-4]
                        if len(exp[0:a]) >= 5 :
                            if exp[a-5] in num :
                                result_mul1 = exp[a-5] + exp[a-4] + exp[a-3] + exp[a-2] + exp[a-1]
                                exp_mul1 = exp[:a-5]
                                if len(exp[0:a]) >= 6 :
                                    if exp[a-6] in num :
                                        result_mul1 = exp[a-6] + exp[a-5] + exp[a-4] + exp[a-3] + exp[a-2] + exp[a-1]
                                        exp_mul1 = exp[:a-6]
                                        if len(exp[0 : a]) >= 7:
                                            if exp[a-7] in num :
                                                result_mul1 = exp[a-7] + exp[a-6] + exp[a-5] + exp[a-4] + exp[a-3] + exp[a-2] + exp[a-1]
                                                exp_mul1 = exp[:a-7]
                                                if len(exp[0:]) >= 8 :
                                                    if exp[a-8] in num :
                                                        result_mul1 =exp[a-8] + exp[a-7] + exp[a-6] + exp[a-5] + exp[a-4] + exp[a-3] + exp[a-2] + exp[a-1]
                                                        exp_mul1 = exp[:a-8]
                                                        if len(exp[0:a]) >= 9 :
                                                            if exp[a-9] in num :
                                                                result_mul1 = exp[a-9] + exp[a-8] + exp[a-7] + exp[a-6] + exp[a-5] + exp[a-4] + exp[a-3] + exp[a-2] + exp[a-1]
                                                                exp_mul1 = exp[:a-9]
                                                                if len(exp[0:a]) >= 10 :
                                                                    if exp[a-10] in num :
                                                                        result_mul1 = exp[a-10] + exp[a-9] + exp[a-8] + exp[a-7] + exp[a-6] + exp[a-5] + exp[a-4] + exp[a-3] + exp[a-2] + exp[a-1]
                                                                        exp_mul1 = exp[:a-10] 

    if exp[a+1] in num :
        result_mul2 = exp[a+1]
        exp_mul2 = exp[a+2:]

        if len(exp[a+1:]) >= 2 :
            if exp[a+2] in num :
                result_mul2 = exp[a+1] + exp[a+2]
                exp_mul2 = exp[a+3:]
                if len(exp[a+1:]) >= 3 :
                    if exp[a+3] in num :
                        result_mul2 = exp[a+1] + exp[a+2] + exp[a+3]
                        exp_mul2 = exp[a+4:]
                        if len(exp[a+1:]) >= 4 :
                            if exp[a+4] in  num: 
                                result_mul2 = exp[a+1] + exp[a+2] + exp[a+3] + exp[a+4]
                                exp_mul2 = exp[a+4:]
                                if len(exp[a+1:]) >= 5 :
                                    if exp[a+5] in  num: 
                                        result_mul2 = exp[a+1] + exp[a+2] + exp[a+3] + exp[a+4] + exp[a+5]
                                        exp_mul2 = exp[a+5:]
                                        if len(exp[a+1:]) >= 6 :
                                            if exp[a+6] in  num: 
                                                result_mul2 = exp[a+1] + exp[a+2] + exp[a+3] + exp[a+4] + exp[a+5] + exp[a+6]
                                                exp_mul2 = exp[a+6:]
                                                if len(exp[a+1 : ]) >= 7:
                                                    if exp[a+7] in num :
                                                        result_mul2 = exp[a+1] + exp[a+2] + exp[a+3] + exp[a+4] + exp[a+5] + exp[a+6] + exp[a+7] 
                                                        exp_mul2 = exp[a+8:]
                                                        if len(exp[a+1 : ]) >= 8:
                                                            if exp[a+8] in num :
                                                                result_mul2 = exp[a+1] + exp[a+2] + exp[a+3] + exp[a+4] + exp[a+5] + exp[a+6] + exp[a+7] + exp[a+8]
                                                                exp_mul2 = exp[a+9:]
                                                                if len(exp[a+1 : ]) >= 9:
                                                                    if exp[a+9] in num :
                                                                        result_mul2 = exp[a+1] + exp[a+2] + exp[a+3] + exp[a+4] + exp[a+5] + exp[a+6] + exp[a+7] + exp[a+8] + exp[a+9]
                                                                        exp_mul2 = exp[a+10:]                                                                             
                                               
    result = round(float(result_mul1)*float(result_mul2),3)   
    value = exp_mul1 + str(result) + exp_mul2             
    return value

def div(exp) :                             #나눗셈 함수
    b = exp.find('/')
    if b == 1:
        result_div1 = exp[b-1]
        exp_div1 = exp[:b-1]
    
    elif b == 2:
        if exp[b-2] in num :
            result_div1 = exp[b-2] + exp[b-1]
            exp_div1 = exp[:b-2]

        elif exp[b-2] in sym :
            result_div1 = exp[b-1]
            exp_div1 = exp[:b-1]

    elif b == 3:
        if exp[b-3] in num :

            result_div1 = exp[b-3] + exp[b-2] + exp[b-1]
            exp_div1 = exp[:b-3]
            
        elif exp[b-2] in num :
            result_div1 = exp[b-2] + exp[b-1]
            exp_div1 = exp[:b-2]

        elif exp[b-2] in sym :
            result_div1 = exp[b-1]
            exp_div1 = exp[:b-1]
    
    elif b >= 4 :
        if exp[b-2] in num :
            result_div1 = exp[b-2] + exp[b-1]
            exp_div1 = exp[:b-2]
            if  exp[b-3] in num :
                result_div1 = exp[b-3] + exp[b-2] + exp[b-1]
                exp_div1 = exp[:b-3]
                if exp[b-4] in num :
                    result_div1 = exp[b-4] + exp[b-3] + exp[b-2] + exp[b-1]
                    exp_div1 = exp[:b-4]
                    if len(exp[0 : b]) >= 5:
                        if exp[b-5] in num :
                            result_div1 = exp[b-5] + exp[b-4] + exp[b-3] + exp[b-2] + exp[b-1]
                            exp_div1 = exp[:b-5] 
                            if len(exp[0 : b]) >= 6:
                                if exp[b-6] in num :
                                    result_div1 = exp[b-6] + exp[b-5] + exp[b-4] + exp[b-3] + exp[b-2] + exp[b-1]
                                    exp_div1 = exp[:b-6]
                                    if len(exp[0 : b]) >= 7:
                                        if exp[b-7] in num :
                                            result_div1 = exp[b-7] + exp[b-6] + exp[b-5] + exp[b-4] + exp[b-3] + exp[b-2] + exp[b-1]
                                            exp_div1 = exp[:b-7]
                                            if len(exp[0:]) >= 8 :
                                                if exp[b-8] in num :
                                                    result_div1 =exp[b-8] + exp[b-7] + exp[b-6] + exp[b-5] + exp[b-4] + exp[b-3] + exp[b-2] + exp[b-1]
                                                    exp_div1 = exp[:b-8]
                                                    if len(exp[0:b]) >= 9 :
                                                        if exp[b-9] in num :
                                                            result_div1 = exp[b-9] + exp[b-8] + exp[b-7] + exp[b-6] + exp[b-5] + exp[b-4] + exp[b-3] + exp[b-2] + exp[b-1]
                                                            exp_div1 = exp[:b-9]
                                                            if len(exp[0:b]) >= 10 :
                                                                if exp[b-10] in num :
                                                                    result_div1 = exp[b-10] + exp[b-9] + exp[b-8] + exp[b-7] + exp[b-6] + exp[b-5] + exp[b-4] + exp[b-3] + exp[b-2] + exp[b-1]
                                                                    exp_div1 = exp[:b-10]   

        elif exp[b-2] in sym :
            result_div1 = exp[b-1]
            exp_div1 = exp[:b-1]    
            
    if exp[b+1] in num :
        result_div2 = exp[b+1]
        exp_div2 = exp[b+2:] 

        if len(exp[b+1 : ]) >= 2:
            if exp[b+2] in  sym :
                result_div2 = exp[b+1]
                exp_div2 = exp[b+2:]        
            elif exp[b+2] in num :                    
                result_div2 = exp[b+1] + exp[b+2]
                exp_div2 = exp[b+3:]
                if len(exp[b+1 : ]) >= 3:
                    if exp[b+3] in num :
                        result_div2 = exp[b+1] + exp[b+2] + exp[b+3]
                        exp_div2 = exp[b+4:]
                        if len(exp[b+1 : ]) >= 4:
                            if exp[b+4] in num :
                                result_div2 = exp[b+1] + exp[b+2] + exp[b+3] + exp[b+4] 
                                exp_div2 = exp[b+5:]
                            if len(exp[b+1 :] ) >= 5:
                                if exp[b+5] in num :
                                    result_div2 = exp[b+1] + exp[b+2] + exp[b+3] + exp[b+4] + exp[b+5]
                                    exp_div2 = exp[b+6:]
                                if len(exp[b+1 :] ) >= 6:
                                    if exp[b+6] in num :
                                        result_div2 = exp[b+1] + exp[b+2] + exp[b+3] + exp[b+4] + exp[b+5] + exp[b+6]
                                        exp_div2 = exp[b+7:]
                                        if len(exp[b+1 : ]) >= 7:
                                            if exp[b+7] in num :
                                                result_div2 = exp[b+1] + exp[b+2] + exp[b+3] + exp[b+4] + exp[b+5] + exp[b+6] + exp[b+7] 
                                                exp_div2 = exp[b+8:]
                                                if len(exp[b+1 : ]) >= 8:
                                                    if exp[b+8] in num :
                                                        result_div2 = exp[b+1] + exp[b+2] + exp[b+3] + exp[b+4] + exp[b+5] + exp[b+6] + exp[b+7] + exp[b+8]
                                                        exp_div2 = exp[b+9:]
                                                        if len(exp[b+1 : ]) >= 9:
                                                            if exp[b+9] in num :
                                                                result_div2 = exp[b+1] + exp[b+2] + exp[b+3] + exp[b+4] + exp[b+5] + exp[b+6] + exp[b+7] + exp[b+8] + exp[b+9]
                                                                exp_div2 = exp[b+10:] 

        else :
            result_div2 = exp[b+1]
            exp_div2 = exp[b+2:]
        
    result = round(float(result_div1)/float(result_div2),3)        
    exp = exp_div1 + str(result) + exp_div2

    return exp

def add(exp) :                             # 덧셈 함수
    c = exp.index('+')                  # 맨 앞 덧셈의 위치                       
                                        #덧셈의 위치가 뺄셈의 위치보다 앞에 있을때 (+ - 순서가 무조건 존재하기 때문에, 같을수는 없음)
    if c == 1:
        result_add1 = exp[c-1]
        exp_add1 = exp[:c-1]

    elif c == 2:            
        if exp[c-2] in num :
            result_add1 = exp[c-2] + exp[c-1]
            exp_add1 = exp[:c-2]
        elif exp[c-2] in sym :
            result_add1 = exp[c-1]
            exp_add1 = exp[:c-1]

    elif c >= 3:                        
        if exp[c-2] in sym :
            result_add1 = exp[c-1]
            exp_add1 = exp[:c-1]
        elif exp[c-2] in num :
            result_add1 = exp[c-2] + exp[c-1]
            exp_add1 = exp[:c-2]
            if exp[c-3] in num :
                result_add1 = exp[c-3] + exp[c-2] + exp[c-1]
                exp_add1 = exp[:c-3]
                if len(exp[0:c]) >= 4 :
                    if exp[c-4] in num :
                        result_add1 = exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                        exp_add1 = exp[:c-4]
                        if len(exp[0:c]) >= 5:
                            if exp[c-5] in num :
                                result_add1 = exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                exp_add1 = exp[:c-5]
                                if len(exp[0:c]) >= 6 :
                                    if exp[c-6] in num :
                                        result_add1 =exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                        exp_add1 = exp[:c-6]
                                        if len(exp[0:c]) >=  7:
                                            if exp[c-7] in num :
                                                result_add1 =exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                exp_add1 = exp[:c-7]
                                                if len(exp[0:c]) >= 8 :
                                                    if exp[c-8] in num :
                                                        result_add1 =exp[c-8] + exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                        exp_add1 = exp[:c-8]
                                                        if len(exp[0:c]) >= 9 :
                                                            if exp[c-9] in num :
                                                                result_add1 = exp[c-9] + exp[c-8] + exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                                exp_add1 = exp[:c-9]
                                                                if len(exp[0:c]) >= 10 :
                                                                    if exp[c-10] in num :
                                                                        result_add1 = exp[c-10] + exp[c-9] + exp[c-8] + exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                                        exp_add1 = exp[:c-10]         

    if exp[c+1] in num :
        result_add2 = exp[c+1]
        exp_add2 = exp[c+2:]
    
        if len(exp[c+1:]) == 2:
            if exp[c+2] in num :
                result_add2 = exp[c+1] + exp[c+2]
                exp_add2 = exp[c+3:]
            elif exp[c+2] in  sym:
                result_add2 = exp[c+1]
                exp_add2 = exp[c+2:]                        
        
        if len(exp[c+1:]) >= 3:    
            result_add2 = exp[c+1]
            exp_add2 = exp[c+2:]
            
            if exp[c+2] in  sym:
                result_add2 = exp[c+1]
                exp_add2 = exp[c+2:]

            elif exp[c+3] in  sym: 
                result_add2 = exp[c+1] + exp[c+2]
                exp_add2 = exp[c+3:]
            
            elif exp[c+3] in num :
                result_add2 = exp[c+1] + exp[c+2] + exp[c+3]
                exp_add2 = exp[c+4:]
                if len(exp[c+1 : ]) >= 4:
                    if exp[c+4] in num :
                        result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4]
                        exp_add2 = exp[c+5:]
                        if len(exp[c+1 : ]) >= 5:
                            if exp[c+5] in num :
                                result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5]
                                exp_add2 = exp[c+6:]
                                if len(exp[c+1 : ]) >= 6:
                                    if exp[c+6] in num :
                                        result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] +  exp[c+5] + exp[c+6]
                                        exp_add2 = exp[c+7:]
                                        if len(exp[c+1 : ]) >= 7:
                                            if exp[c+7] in num :
                                                result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] 
                                                exp_add2 = exp[c+8:]
                                                if len(exp[c+1 : ]) >= 8:
                                                    if exp[c+8] in num :
                                                        result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] + exp[c+8]
                                                        exp_add2 = exp[c+9:]
                                                        if len(exp[c+1 : ]) >= 9:
                                                            if exp[c+9] in num :
                                                                result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] + exp[c+8] + exp[c+9]
                                                                exp_add2 = exp[c+10:]

    result = round(float(result_add1)+float(result_add2),4)        
    exp = exp_add1 + str(result) + exp_add2

    return exp

def min(exp) :                              #뺄셈 함수
    d = exp.index('-')
    
    if d == 1:
        result_min1 = exp[d-1]
        exp_min1 = exp[:d-1]
    
    elif d == 2:
        if exp[d-2] in num :
            result_min1 = exp[d-2] + exp[d-1]
            exp_min1 = exp[:d-2]

        elif exp[d-2] in sym :
            result_min1 = exp[d-1]
            exp_min1 = exp[:d-1]

    elif d >= 3:
        if exp[d-3] in num :
            result_min1 = exp[d-3] + exp[d-2] + exp[d-1]
            exp_min1 = exp[:d-3]
            if len(exp[0 : d]) >= 4 :
                if exp[d-4] in num :
                    result_min1 =  exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                    exp_min1 = exp[:d-4]
                    if len(exp[0 : d]) >= 5 :
                        if exp[d-5] in num :
                            result_min1 = exp[d-5] + exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                            exp_min1 = exp[:d-5]
                            if len(exp[0 : d]) >= 6 :
                                if exp[d-6] in num :
                                    result_min1 =  exp[d-6] + exp[d-5] + exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                                    exp_min1 = exp[:d-6]
                                    if len(exp[0 : d]) >= 7 :
                                        if exp[d-7] in num :
                                            result_min1 = exp[d-7] + exp[d-6] + exp[d-5] + exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                                            exp_min1 = exp[:d-7]
                                            if len(exp[0 : d]) >= 8 :
                                                if exp[d-8] in num :
                                                    result_min1 =  exp[d-8] + exp[d-7] + exp[d-6] + exp[d-5] + exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                                                    exp_min1 = exp[:d-8]
                                                    if len(exp[0 : d]) >= 9 :
                                                        if exp[d-9] in num :
                                                            result_min1 =  exp[d-9] + exp[d-8] + exp[d-7] + exp[d-6] + exp[d-5] + exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                                                            exp_min1 = exp[:d-9]
            
        elif exp[d-2] in num :
            result_min1 = exp[d-2] + exp[d-1]
            exp_min1 = exp[:d-2]

        elif exp[d-2] in sym :
            result_min1 = exp[d-1]
            exp_min1 = exp[:d-1]

    if exp[d+1] in num :
        result_min2 = exp[d+1]
        exp_min2 = exp[d+2:] 
        if len(exp[d+1:]) >= 2:
            if exp[d+2] in num :
                result_min2 = exp[d+1] + exp[d+2]
                exp_min2 = exp[d+3:]
                if len(exp[d+1:]) >= 3:
                    if exp[d+3] in num :
                        result_min2 = exp[d+1] + exp[d+2] + exp[d+3]
                        exp_min2 = exp[d+4:]
                        if len(exp[d+1:]) >= 4:
                            if exp[d+4] in num :
                                result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4]
                                exp_min2 = exp[d+5:]
                                if len(exp[d+1:]) >= 5:
                                    if exp[d+5] in num :
                                        result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4] + exp[d+5]
                                        exp_min2 = exp[d+6:]
                                        if len(exp[d+1:]) >= 6:
                                            if exp[d+6] in num :
                                                result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4] + exp[d+5] + exp[d+6]
                                                exp_min2 = exp[d+7:]
                                                if len(exp[d+1:]) >= 7:
                                                    if exp[d+7] in num :
                                                        result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4] + exp[d+5] + exp[d+6] + exp[d+7]
                                                        exp_min2 = exp[d+8:]
                                                        if len(exp[d+1:]) >= 8:
                                                            if exp[d+8] in num :
                                                                result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4] + exp[d+5] + exp[d+6] + exp[d+7] + exp[d+8]
                                                                exp_min2 = exp[d+9:]
                                                                if len(exp[d+1:]) >= 9:
                                                                    if exp[d+9] in num :
                                                                        result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4] + exp[d+5] + exp[d+6] + exp[d+7] + exp[d+8] + exp[d+9]
                                                                        exp_min2 = exp[d+10:]


    result = round(float(result_min1)-float(result_min2),3)            
    exp = exp_min1 + str(result) + exp_min2
   
    return exp

def min_add(exp) :                      # 맨앞) 뺄셈 덧셈 ... 
    c = exp.index('+')                  # 맨 앞 덧셈의 위치   
    d = exp.index('-')
    if d == 0 :                         # 식 맨 앞에 -가 있다면, (음수 처리 하기 위해)
        count_5 = exp.count('-')        # 뺄셈 개수 
        count_6 = exp.count('+')        # 덧셈 개수
        if count_5 >= 2:                    # 뺄셈 두개 이상!!! 
            dd = exp[d+1:].index('-')       # (맨앞)뺄셈 뺄셈과 덧셈 있는 경우,
            if c <= dd :                 #-6.3 + 9 - 7.3 뺄셈 덧셈 뺄셈 
                if c == 1:      
                    result_add1 = exp[c-1]
                    exp_add1 = exp[1:c-1]

                elif c == 2:
                    if exp[c-2] in num :
                        result_add1 = exp[c-2] + exp[c-1]
                        exp_add1 = exp[:c-2]
                    elif exp[c-2] in sym :
                        result_add1 = exp[c-1]
                        exp_add1 = exp[1:c-1]

                elif c >= 3:
                    if exp[c-2] in sym :
                        result_add1 = exp[c-1]
                        exp_add1 = exp[:c-1]
                    elif exp[c-2] in num :
                        result_add1 = exp[c-2] + exp[c-1]
                        exp_add1 = exp[:c-2]
                        if exp[c-3] in num :
                            result_add1 = exp[c-3] + exp[c-2] + exp[c-1]
                            exp_add1 = exp[:c-3]
                            if len(exp[0:c]) >= 4 :
                                if exp[c-4] in num :
                                    result_add1 = exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                    exp_add1 = exp[:c-4]
                                    if len(exp[0:c]) >= 5:
                                        if exp[c-5] in num :
                                            result_add1 = exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                            exp_add1 = exp[:c-5]
                                            if len(exp[0:c]) >= 6 :
                                                if exp[c-6] in num :
                                                    result_add1 =exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                    exp_add1 = exp[:c-6]
                                                    if len(exp[0:c]) >=  7:
                                                        if exp[c-7] in num :
                                                            result_add1 =exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                            exp_add1 = exp[:c-7]
                                                            if len(exp[0:c]) >= 8 :
                                                                if exp[c-8] in num :
                                                                    result_add1 =exp[c-8] + exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                                    exp_add1 = exp[:c-8]
                                                                    if len(exp[0:c]) >= 9 :
                                                                        if exp[c-9] in num :
                                                                            result_add1 = exp[c-9] + exp[c-8] + exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                                            exp_add1 = exp[:c-9]
                                                                            if len(exp[0:c]) >= 10 :
                                                                                if exp[c-10] in num :
                                                                                    result_add1 = exp[c-10] + exp[c-9] + exp[c-8] + exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                                                    exp_add1 = exp[:c-10]         

                if exp[c+1] in num :
                    result_add2 = exp[c+1]
                    exp_add2 = exp[c+2:]
                
                    if len(exp[c+1:]) == 2:
                        if exp[c+2] in num :
                            result_add2 = exp[c+1] + exp[c+2]
                            exp_add2 = exp[c+3:]
                        elif exp[c+2] in  sym:
                            result_add2 = exp[c+1]
                            exp_add2 = exp[c+2:]                        
                    
                    if len(exp[c+1:]) >= 3:    
                        result_add2 = exp[c+1]
                        exp_add2 = exp[c+2:]
                        
                        if exp[c+2] in  sym:
                            result_add2 = exp[c+1]
                            exp_add2 = exp[c+2:]

                        elif exp[c+3] in  sym: 
                            result_add2 = exp[c+1] + exp[c+2]
                            exp_add2 = exp[c+3:]
                        
                        elif exp[c+3] in num :
                            result_add2 = exp[c+1] + exp[c+2] + exp[c+3]
                            exp_add2 = exp[c+4:]
                            if len(exp[c+1 : ]) >= 4:
                                if exp[c+4] in num :
                                    result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4]
                                    exp_add2 = exp[c+5:]
                                    if len(exp[c+1 : ]) >= 5:
                                        if exp[c+5] in num :
                                            result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5]
                                            exp_add2 = exp[c+6:]
                                            if len(exp[c+1 : ]) >= 6:
                                                if exp[c+6] in num :
                                                    result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] +  exp[c+5] + exp[c+6]
                                                    exp_add2 = exp[c+7:]
                                                    if len(exp[c+1 : ]) >= 7:
                                                        if exp[c+7] in num :
                                                            result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] 
                                                            exp_add2 = exp[c+8:]
                                                            if len(exp[c+1 : ]) >= 8:
                                                                if exp[c+8] in num :
                                                                    result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] + exp[c+8]
                                                                    exp_add2 = exp[c+9:]
                                                                    if len(exp[c+1 : ]) >= 9:
                                                                        if exp[c+9] in num :
                                                                            result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] + exp[c+8] + exp[c+9]
                                                                            exp_add2 = exp[c+10:]

                result = round(float(result_add2)- float(result_add1), 4)
                    
                if result == 0 :
                    exp = exp_add1 + exp_add2
                    return exp
                if result >= 0:
                    if exp_add1 == '-':
                        exp = str(result) + exp_add2
                        return exp
                    else:    
                        exp = exp_add1 + str(result) + exp_add2
                        return exp
                if result <= 0:
                    if exp_add1 == '-':
                        exp = str(result) + exp_add2
                        return exp
                    else :
                        exp = exp_add1  +str(result) + exp_add2
                        return exp
        
            elif not exp[dd+1 : c ] in sym :    # 뺄셈 뺄셈 덧셈
                result_exp_min_add1 = exp[dd+2 : c]
                exp_min_add1 = exp[d :dd+1]
                if exp[c+1] in num :
                    result_add2 = exp[c+1]
                    exp_add2 = exp[c+2:]
                
                    if len(exp[c+1:]) == 2:
                        if exp[c+2] in num :
                            result_add2 = exp[c+1] + exp[c+2]
                            exp_add2 = exp[c+3:]
                        elif exp[c+2] in  sym:
                            result_add2 = exp[c+1]
                            exp_add2 = exp[c+2:]                        
                    
                    if len(exp[c+1:]) >= 3:    
                        result_add2 = exp[c+1]
                        exp_add2 = exp[c+2:]
                        
                        if exp[c+2] in  sym:
                            result_add2 = exp[c+1]
                            exp_add2 = exp[c+2:]

                        elif exp[c+3] in  sym: 
                            result_add2 = exp[c+1] + exp[c+2]
                            exp_add2 = exp[c+3:]
                        
                        elif exp[c+3] in num :
                            result_add2 = exp[c+1] + exp[c+2] + exp[c+3]
                            exp_add2 = exp[c+4:]
                            if len(exp[c+1 : ]) >= 4:
                                if exp[c+4] in num :
                                    result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4]
                                    exp_add2 = exp[c+5:]
                                    if len(exp[c+1 : ]) >= 5:
                                        if exp[c+5] in num :
                                            result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5]
                                            exp_add2 = exp[c+6:]
                                            if len(exp[c+1 : ]) >= 6:
                                                if exp[c+6] in num :
                                                    result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] +  exp[c+5] + exp[c+6]
                                                    exp_add2 = exp[c+7:]
                                                    if len(exp[c+1 : ]) >= 7:
                                                        if exp[c+7] in num :
                                                            result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] 
                                                            exp_add2 = exp[c+8:]
                                                            if len(exp[c+1 : ]) >= 8:
                                                                if exp[c+8] in num :
                                                                    result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] + exp[c+8]
                                                                    exp_add2 = exp[c+9:]
                                                                    if len(exp[c+1 : ]) >= 9:
                                                                        if exp[c+9] in num :
                                                                            result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] + exp[c+8] + exp[c+9]
                                                                            exp_add2 = exp[c+10:]

                result = round(float(result_add2) - float(result_exp_min_add1),4)
                if result == 0 :
                    exp = exp_min_add1 + exp_add2
                    return exp
                if result >= 0:
                    exp = exp_min_add1 +'+'+ str(result) + exp_add2
                    return exp
                if result <= 0:
                    if exp_min_add1 == '-':
                        exp = str(result) + exp_add2
                    else :
                        exp = exp_min_add1  +str(result) + exp_add2
                    return exp  

        








        elif count_5 == 1 and count_6 >= 1 : # 맨 앞)뺄셈 그리고 더하기  ex) -7+45 
            if c == 1:      
                result_add1 = exp[c-1]
                exp_add1 = exp[1:c-1]

            elif c == 2:
                if exp[c-2] in num :
                    result_add1 = exp[c-2] + exp[c-1]
                    exp_add1 = exp[:c-2]
                elif exp[c-2] in sym :
                    result_add1 = exp[c-1]
                    exp_add1 = exp[1:c-1]

            elif c >= 3:
                if exp[c-2] in sym :
                    result_add1 = exp[c-1]
                    exp_add1 = exp[:c-1]
                elif exp[c-2] in num :
                    result_add1 = exp[c-2] + exp[c-1]
                    exp_add1 = exp[:c-2]
                    if exp[c-3] in num :
                        result_add1 = exp[c-3] + exp[c-2] + exp[c-1]
                        exp_add1 = exp[:c-3]
                        if len(exp[0:c]) >= 4 :
                            if exp[c-4] in num :
                                result_add1 = exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                exp_add1 = exp[:c-4]
                                if len(exp[0:c]) >= 5:
                                    if exp[c-5] in num :
                                        result_add1 = exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                        exp_add1 = exp[:c-5]
                                        if len(exp[0:c]) >= 6 :
                                            if exp[c-6] in num :
                                                result_add1 =exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                exp_add1 = exp[:c-6]
                                                if len(exp[0:c]) >=  7:
                                                    if exp[c-7] in num :
                                                        result_add1 =exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                        exp_add1 = exp[:c-7]
                                                        if len(exp[0:c]) >= 8 :
                                                            if exp[c-8] in num :
                                                                result_add1 =exp[c-8] + exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                                exp_add1 = exp[:c-8]
                                                                if len(exp[0:c]) >= 9 :
                                                                    if exp[c-9] in num :
                                                                        result_add1 = exp[c-9] + exp[c-8] + exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                                        exp_add1 = exp[:c-9]
                                                                        if len(exp[0:c]) >= 10 :
                                                                            if exp[c-10] in num :
                                                                                result_add1 = exp[c-10] + exp[c-9] + exp[c-8] + exp[c-7] + exp[c-6] + exp[c-5] + exp[c-4] + exp[c-3] + exp[c-2] + exp[c-1]
                                                                                exp_add1 = exp[:c-10]         

            if exp[c+1] in num :
                result_add2 = exp[c+1]
                exp_add2 = exp[c+2:]
            
                if len(exp[c+1:]) == 2:
                    if exp[c+2] in num :
                        result_add2 = exp[c+1] + exp[c+2]
                        exp_add2 = exp[c+3:]
                    elif exp[c+2] in  sym:
                        result_add2 = exp[c+1]
                        exp_add2 = exp[c+2:]                        
                
                if len(exp[c+1:]) >= 3:    
                    result_add2 = exp[c+1]
                    exp_add2 = exp[c+2:]
                    
                    if exp[c+2] in  sym:
                        result_add2 = exp[c+1]
                        exp_add2 = exp[c+2:]

                    elif exp[c+3] in  sym: 
                        result_add2 = exp[c+1] + exp[c+2]
                        exp_add2 = exp[c+3:]
                    
                    elif exp[c+3] in num :
                        result_add2 = exp[c+1] + exp[c+2] + exp[c+3]
                        exp_add2 = exp[c+4:]
                        if len(exp[c+1 : ]) >= 4:
                            if exp[c+4] in num :
                                result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4]
                                exp_add2 = exp[c+5:]
                                if len(exp[c+1 : ]) >= 5:
                                    if exp[c+5] in num :
                                        result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5]
                                        exp_add2 = exp[c+6:]
                                        if len(exp[c+1 : ]) >= 6:
                                            if exp[c+6] in num :
                                                result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] +  exp[c+5] + exp[c+6]
                                                exp_add2 = exp[c+7:]
                                                if len(exp[c+1 : ]) >= 7:
                                                    if exp[c+7] in num :
                                                        result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] 
                                                        exp_add2 = exp[c+8:]
                                                        if len(exp[c+1 : ]) >= 8:
                                                            if exp[c+8] in num :
                                                                result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] + exp[c+8]
                                                                exp_add2 = exp[c+9:]
                                                                if len(exp[c+1 : ]) >= 9:
                                                                    if exp[c+9] in num :
                                                                        result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] + exp[c+8] + exp[c+9]
                                                                        exp_add2 = exp[c+10:]

            result = round(float(result_add2)- float(result_add1), 4)            
            if result == 0 :
                exp = exp_add1 + exp_add2
                return exp
            if result >= 0:
                if exp_add1 == '-':
                    exp = str(result) + exp_add2
                    return exp
                else:    
                    exp = exp_add1 + str(result) + exp_add2
                    return exp
            if result <= 0:
                if exp_add1 == '-':
                    exp = str(result) + exp_add2
                    return exp
                else :
                    exp = exp_add1  +str(result) + exp_add2
                    return exp
    
    if exp[c+1] in num :
        result_add2 = exp[c+1]
        exp_add2 = exp[c+2:]
    
        if len(exp[c+1:]) == 2:
            if exp[c+2] in num :
                result_add2 = exp[c+1] + exp[c+2]
                exp_add2 = exp[c+3:]
            elif exp[c+2] in  sym:
                result_add2 = exp[c+1]
                exp_add2 = exp[c+2:]                        
        
        if len(exp[c+1:]) >= 3:    
            result_add2 = exp[c+1]
            exp_add2 = exp[c+2:]
            
            if exp[c+2] in  sym:
                result_add2 = exp[c+1]
                exp_add2 = exp[c+2:]

            elif exp[c+3] in  sym: 
                result_add2 = exp[c+1] + exp[c+2]
                exp_add2 = exp[c+3:]
            
            elif exp[c+3] in num :
                result_add2 = exp[c+1] + exp[c+2] + exp[c+3]
                exp_add2 = exp[c+4:]
                if len(exp[c+1 : ]) >= 4:
                    if exp[c+4] in num :
                        result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4]
                        exp_add2 = exp[c+5:]
                        if len(exp[c+1 : ]) >= 5:
                            if exp[c+5] in num :
                                result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5]
                                exp_add2 = exp[c+6:]
                                if len(exp[c+1 : ]) >= 6:
                                    if exp[c+6] in num :
                                        result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] +  exp[c+5] + exp[c+6]
                                        exp_add2 = exp[c+7:]
                                        if len(exp[c+1 : ]) >= 7:
                                            if exp[c+7] in num :
                                                result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] 
                                                exp_add2 = exp[c+8:]
                                                if len(exp[c+1 : ]) >= 8:
                                                    if exp[c+8] in num :
                                                        result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] + exp[c+8]
                                                        exp_add2 = exp[c+9:]
                                                        if len(exp[c+1 : ]) >= 9:
                                                            if exp[c+9] in num :
                                                                result_add2 = exp[c+1] + exp[c+2] + exp[c+3] + exp[c+4] + exp[c+5] + exp[c+6] + exp[c+7] + exp[c+8] + exp[c+9]
                                                                exp_add2 = exp[c+10:]
     
    result = round( float(result_add2)- float( result_exp_min_add1) ,4 )
    if result >= 0 :
        exp = exp_min_add1 + '+' + str(result) + exp_add2
        return exp
    #elif result <= 0 :
    #    exp = exp_min_add1 + '-' + str(result) + exp_add2
    elif result == 0 :
        exp = exp_min_add1 + '0' + exp_add2
        return exp

    return exp

def min_min(exp) :                      # 맨앞) 뺄셈 뺄셈 뺄셈
    d = exp[1:].index('-') + 1

    if d == 1:
        result_min1 = exp[d-1]
        exp_min1 = exp[:d-1]
    
    elif d == 2:
        if exp[d-2] in num :
            result_min1 = exp[d-2] + exp[d-1]
            exp_min1 = exp[:d-2]

        elif exp[d-2] in sym :
            result_min1 = exp[d-1]
            exp_min1 = exp[:d-1]

    elif d >= 3:
        if exp[d-3] in num :
            result_min1 = exp[d-3] + exp[d-2] + exp[d-1]
            exp_min1 = exp[:d-3]
            if len(exp[0 : d]) >= 4 :
                if exp[d-4] in num :
                    result_min1 =  exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                    exp_min1 = exp[:d-4]
                    if len(exp[0 : d]) >= 5 :
                        if exp[d-5] in num :
                            result_min1 = exp[d-5] + exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                            exp_min1 = exp[:d-5]
                            if len(exp[0 : d]) >= 6 :
                                if exp[d-6] in num :
                                    result_min1 =  exp[d-6] + exp[d-5] + exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                                    exp_min1 = exp[:d-6]
                                    if len(exp[0 : d]) >= 7 :
                                        if exp[d-7] in num :
                                            result_min1 = exp[d-7] + exp[d-6] + exp[d-5] + exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                                            exp_min1 = exp[:d-7]
                                            if len(exp[0 : d]) >= 8 :
                                                if exp[d-8] in num :
                                                    result_min1 =  exp[d-8] + exp[d-7] + exp[d-6] + exp[d-5] + exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                                                    exp_min1 = exp[:d-8]
                                                    if len(exp[0 : d]) >= 9 :
                                                        if exp[d-9] in num :
                                                            result_min1 =  exp[d-9] + exp[d-8] + exp[d-7] + exp[d-6] + exp[d-5] + exp[d-4] + exp[d-3] + exp[d-2] + exp[d-1]
                                                            exp_min1 = exp[:d-9]
            
        elif exp[d-2] in num :
            result_min1 = exp[d-2] + exp[d-1]
            exp_min1 = exp[:d-2]

        elif exp[d-2] in sym :
            result_min1 = exp[d-1]
            exp_min1 = exp[:d-1]

    if exp[d+1] in num :
        result_min2 = exp[d+1]
        exp_min2 = exp[d+2:] 
        if len(exp[d+1:]) >= 2:
            if exp[d+2] in num :
                result_min2 = exp[d+1] + exp[d+2]
                exp_min2 = exp[d+3:]
                if len(exp[d+1:]) >= 3:
                    if exp[d+3] in num :
                        result_min2 = exp[d+1] + exp[d+2] + exp[d+3]
                        exp_min2 = exp[d+4:]
                        if len(exp[d+1:]) >= 4:
                            if exp[d+4] in num :
                                result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4]
                                exp_min2 = exp[d+5:]
                                if len(exp[d+1:]) >= 5:
                                    if exp[d+5] in num :
                                        result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4] + exp[d+5]
                                        exp_min2 = exp[d+6:]
                                        if len(exp[d+1:]) >= 6:
                                            if exp[d+6] in num :
                                                result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4] + exp[d+5] + exp[d+6]
                                                exp_min2 = exp[d+7:]
                                                if len(exp[d+1:]) >= 7:
                                                    if exp[d+7] in num :
                                                        result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4] + exp[d+5] + exp[d+6] + exp[d+7]
                                                        exp_min2 = exp[d+8:]
                                                        if len(exp[d+1:]) >= 8:
                                                            if exp[d+8] in num :
                                                                result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4] + exp[d+5] + exp[d+6] + exp[d+7] + exp[d+8]
                                                                exp_min2 = exp[d+9:]
                                                                if len(exp[d+1:]) >= 9:
                                                                    if exp[d+9] in num :
                                                                        result_min2 = exp[d+1] + exp[d+2] + exp[d+3] + exp[d+4] + exp[d+5] + exp[d+6] + exp[d+7] + exp[d+8] + exp[d+9]
                                                                        exp_min2 = exp[d+10:]
    result = round(float(result_min1)+float(result_min2),3)            
    exp = exp_min1 + str(result) + exp_min2
    return exp

def calc(exp):
    while str('*') or str('/')  in exp :        #입력된 식에 곱셈, 나눗셈 있을 경우
        count_1 = exp.count('*')                #곱셈 개수 
        count_2 = exp.count('/')                #나눗셈 개수

        if count_1 and count_2 >= 1 :           #곱셈 O 나눗셈 O
            a = exp.find('*')                      #곱셈의 처음 위치
            b = exp.find('/')                      #나눗셈의 처음 위치

            if b >= a :                         # 곱셈이 나눗셈보다 앞에 있을 때,
                exp = mul(exp)
                
            elif a >= b :                       # 나눗셈이 곱셈보다 앞에 있을 때,
                exp = div(exp)
                   
        elif count_1 >= 1 and count_2 == 0:     #곱셈 O 나눗셈 X 
            exp = mul(exp)
                        
        elif count_1 == 0 and count_2 >= 1:     #곱셈 X 나눗셈 O
            exp = div(exp)
            
        else :                                  #곱셈 X 나눗셈 X
            break
    
    while str('+') or str('-') in exp :           #식에 덧셈, 뺄셈이 있는 경우
        count_3 = exp.count('+')
        count_4 = exp.count('-')
        
        if count_3 and count_4 >= 1 :            #덧셈 O , 뺄셈 O
            c = exp.index('+')                   #덧셈의 맨 앞 위치
            d = exp.index('-')                   #뺄셈의 맨 앞 위치
            
            if d == 0 :                  # 뺄셈이 맨 앞에 있고 덧셈이 존재하는 경우, 뺄셈을 음수 처리
                exp = min_add(exp)

            elif  d >= c :               #덧셈이 뺄셈보다 앞에 있을 때, 뺄셈이 맨 앞에 있을 때 (음수)
                exp = add(exp)
                
            elif c >= d :                        #뺄셈이 덧셈보다 앞에 있을 때
               exp = min(exp)
            
        elif count_3 >= 1 and count_4 == 0 :     #덧셈 O , 뺄셈 X   
            c = exp.index('+')
            exp = add(exp)
            
        elif count_3 == 0 and count_4 >= 1 :     #덧셈 X , 뺄셈 O
            d = exp.index('-')
            if d == 0 :
                if count_4 >=2 :                 # 뺄셈 뺄셈 ..                                        
                    exp = min_min(exp)
                elif not exp[1:]  in sym:                
                    return exp
            else : 
                exp = min(exp)

        
        else :                                   #덧셈 X , 뺄셈 X
            break

    value = exp
    if input == '0':
        value = int(0)
    
    return value

value = calc(in_put)
print(value)