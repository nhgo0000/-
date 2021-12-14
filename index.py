import re
jds = "f'(x) = "

def is_digit(n): #입력 된 값이 숫자열인지 구분
    try: #아래의 명령문 시도
        asd = float(n) #asd 라는 임의의 변수 입력된 n 값 float로 바꿈
        return True #성공 시 True 값 반환 
    except ValueError: #try에서 명령문 실패 시 작동 
        return False # False 값 반환
    
def 미분계산기(): #함수 선언
    a = input("최고 차항 입력 : ") #입력 값 a에 저장
    if a == "0":
        print(jds + a)
            
    elif a.isdigit() == False: # 만약 a가 숫자가 아니라면
        print("숫자를 입력하시오") #출력 
        미분계산기() #함수 재실행 
    else: # a가 숫자라면
        a = int(a) # a를 int 형식으로 수정 
        미분함수(a) #미분함수(a)를 실행 

def 미분함수(a): 
    l = a 
    x = l
    while l != 0: 
        
        n = input(str(l)+"차항의 계수 : ") 
    
        
        if is_digit(n) == False:
            print("숫자를 입력하시오")

        else:
            
            n = int(n) 
            
            if l == x:  
                if n != 0:
                    
                    if l == 2:
                            num = str(n * l) + "x"
                            
                    elif l == 1:
                            num = str(n * l)
                            
                    else:
                            num = str(n * l) + "x^{}".format(l-1)
                    
                else: 
                    num = "" 
                    
            else: 
                
                if num == "": 
                    if n != 0:  
                        if l == 2: 
                            num = str(n * l) + "x" 
                            
                        elif l == 1:
                            num = str(n * l)
                            
                        else:
                            num = str(n * l) + "x^{}".format(l-1)
                            
                    else:
                        num = num
                        
                else:
                    if n != 0:
                        if l == 2:
                            num = num + " + " + str(n * l) + "x"
                            
                        elif l == 1:
                            num = num + " + " + str(n * l)
                            
                        else:
                            num = num + " + " + str(n * l) + "x^{}".format(l-1)
                            
                    else:
                        num = num
                    
            l = l - 1
            
    def sang():
        
        delete = input("상수항의 계수 : ")
        
        if is_digit(delete) == False:
            print("숫자를 입력하시오")
            sang()
            
        else:
            pass
    
    sang()
    if num == "":
        print(jds + "0")
    else:
        print(jds + num)

미분계산기()
    
