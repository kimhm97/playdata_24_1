'''

    포맷출력

   예> 이름: 홍길동, 나이:20, 주소: 서울
       이름: 이순신, 나이:30, 주소: 부산

   1.  변수 = "이름:{}   나이:{}   주소:{}  ".format("홍길동",20,"서울") 함수

       # 위치 지정, 여러번 지정 가능
   2.  변수 = "이름:{0}   나이:{1}   주소:{2}  ".format("홍길동",20,"서울") 함수

   3.  * key=value 형식 (매우 중요)
        변수 = "이름:{name}   나이:{age}   주소:{address}  ".format(name="홍길동",age=20, address="서울") 함수

   4.  혼합 가능 (매우 중요)
'''
mesg = "이름:{} 나이:{} 주소:{}".format("홍길동",20,"서울")
print(mesg)

mesg = "이름:{1} 나이:{0} 주소:{2}".format("홍길동",20,"서울")
print(mesg)
mesg = "이름:{1} 나이:{0} 주소:{2}, {2}, {2}".format("홍길동",20,"서울")
print(mesg)
mesg = "이름:{name}   나이:{age}   주소:{address}  ".format(name="홍길동",age=20, address="서울")
print(mesg)

mesg = "이름:{0}   나이:{1}   주소:{address}  ".format("홍길동", 20, address="서울")
print(mesg)