'''

   1. packing
      값,값2,...  ====> 집합형

   2. unpacking ==> *집합형 ( dict제외 )
     집합형 ===> 값 , 값2, ,....
'''

# 1. unpacking 이해
print("hello") # hello
print(*"hello") # h e l l o

print([10,20,30]) # [10, 20, 30]
print(*[10,20,30]) # 10 20 30 print(10,20,30)동일

# 2. "{},{},...".format( *값 )
x = [10,20,30]
mesg = "값1:{}, 값2:{}, 값3:{}".format(x[0], x[1], x[2])
print(mesg)

mesg = "값1:{}, 값2:{}, 값3:{}".format(*x)
print(mesg)

# 3. "{}, {}".format( **dict )
y = {"username":"홍길동","age":20}

mesg = "값1:{username}, 값2:{age}".format(**y) #  format(username="홍길동", age=20 ) 와 동일
print(mesg)