

# 이스케이프 문자 ( escape )를 무시 ==> raw string
print("HelloWorld")
print("Hello\nWorld") # \n은 라인변경
print(r"Hello\nWorld")
print()
print("Hello   World")
print("Hello\tWorld") # \t 은 탭을 3 입력한 효과와 동일
print(r"Hello\tWorld")
print()

print("Hello\'World") # Hello'World 출력하기를 원한다.
print(r"Hello\'World")
print('Hello\'World') # Hello'World 출력하기를 원한다.
print(r'Hello\'World')

print()

print("Hello\"World") # Hello"World 출력하기를 원한다.
print(r"Hello\"World")
print('Hello\"World') # Hello"World 출력하기를 원한다.
print(r'Hello\"World')

print()
# print("C:\Python38") # 경로지정시 주로 사용.  하나의 \ 지정해도 가능하지만 OS에 따라서 에러가 발생될 수도 있다.
print("C:\\Python38") # 경로지정시 주로 사용.
print(r"C:\\Python38")