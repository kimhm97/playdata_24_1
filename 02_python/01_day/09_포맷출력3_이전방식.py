'''
   포맷 출력

   1. "".format(값) 방식 ==> 권장

   2. 이전 방식
      "이름:%s  나이:%d 키:%.2f    성별:%c  " %  ( "홍길동", 20, 177.424, "남" )

      %s: 문자열
      %d: 정수
      %f: 실수
      %c: 문자하나

'''
mesg = "이름:%s  나이:%d 키:%.2f    성별:%c  " %  ( "홍길동", 20, 177.424, "남" )
print(mesg)