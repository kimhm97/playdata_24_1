'''
   포맷 출력 3가지 방법

   1. "".format(값) 방식 ==> 권장

   2. 이전 방식
      "이름:%s  나이:%d 키:%.2f    성별:%c  " %  ( "홍길동", 20, 177.424, "남" )

      %s: 문자열
      %d: 정수
      %f: 실수
      %c: 문자하나

   3. format string
    ==>  f"" 형식
    ==> 장점은 ""안에 변수사용 가능
'''
name = "홍길동"
age = 20
mesg = "이름: {name}, 나이:{age}"
print(mesg)
mesg = f"이름: {name}, 나이:{age}"
print(mesg)



