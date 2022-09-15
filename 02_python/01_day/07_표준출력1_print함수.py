'''
   표준출력
   1. print() 함수 이용
    help(print)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)


'''
# help(print)

# 1. 값을 여러개 사용 가능
print(10)
print(10,20,30)

# 2. 여러 값 출력시 구분자는 기본적으로 공백 적용 ==> 커스터마이징 가능
print(10,20,30)  # 10 20 30
print(10,20,30, sep=',')  # 10,20,30
print(10,20,30, sep=':')  # 10:20:30
print()
# 3. print는 기본적으로 새로운 라인에 출력됨. ==> 커스터마이징 가능
print(10,20,30, end=" ")
print(100,200)
print()

# 4. 모두 적용 가능
print(1,2,3, sep=":", end=" ")
print(10,20,30)

# 5.모니터 출력 대신에 파일에 출력 ==> 커스터마이징 가능
with open("c:\\a.txt", "w") as f:
    print("HelloWorld", file = f)






