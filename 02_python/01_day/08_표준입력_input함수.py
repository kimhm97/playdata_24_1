'''
   표준 입력
   1.input() 함수 이용
    help(input)
    Read a string from standard input


   2. "20" --> 20 변환함수
     int("20") ---> 20
'''
help(input)
name = input("이름입력")
print("입력된 이름:",name)
age = input("나이 입력:\n")
print("입력된 나이:", age)
print("내년 나이:", int(age)+1 )


