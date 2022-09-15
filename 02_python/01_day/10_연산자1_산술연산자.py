'''

  연산자

  1. 산술연산자
    +, -, *, / , %, //, ** (제곱)

   # 2가지 연산자
   문자 + 문자 ==> 연결
   문자 * 숫자 ==>

   # 함수 ==> 몫과 나머지 한번에 구하기
     divmod(10, 3)

'''
n = 10
n2 = 3
print("+", n+n2)  # 13
print("-", n-n2)  # 7
print("*", n*n2)  # 30
print("/", n/n2)  # 3.3333333333333335
print("//", n//n2) # 3
print("%", n%n2) # 1
print("**", n**n2) # 1000

print("hellow"+"world") # hellowworld
print("#" * 10) # ##########

# divmod(10,3)
print(divmod(10, 3)) # (3, 1) 튜플 형식으로 반환

k = 300,100 # (300,100) 튜플로 처리
print(k)
k2, k3 = 300, 100
print(k2, k3)

# 매우 중요하다.
x, y = divmod(10, 3) # (3, 1)
x, y = (3, 1)
print("몫:{}, 나머자:{}".format(x, y))