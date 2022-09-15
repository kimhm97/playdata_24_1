'''

    변수에 저장된 데이터의 타입 비교
    None 타입 비교시 isinstance() 사용못하고  is None 연산자 사용한다.
'''
# 1. 변수에 저장된 데이터의 타입 비교
int_value = 10
float_value = 3.14
bool_value = True
none_value = None

print("int_value 변수에 저장된 데이터타입이 int가 맞아?", isinstance(int_value, int)) # True
print("int_value 변수에 저장된 데이터타입이 str가 맞아?", isinstance(int_value, str)) # False
print("none_value 변수에 저장된 데이터타입이 None가 맞아?", none_value is None ) # True

str_value = "Hello"
list_value = [10,20]
tuple_value = (10,20)
set_value = {10, 20}
dict_value ={"name":"홍길동","age":20}

print("str_value 변수에 저장된 데이터타입이 str가 맞아?", isinstance(str_value, str)) # True
print("list_value 변수에 저장된 데이터타입이 list가 맞아?", isinstance(list_value, list)) # True
print("tuple_value 변수에 저장된 데이터타입이 tuple가 맞아?", isinstance(tuple_value, tuple)) # True
print("set_value 변수에 저장된 데이터타입이 set가 맞아?", isinstance(set_value, set)) # True
print("dict_value 변수에 저장된 데이터타입이 dict가 맞아?", isinstance(dict_value, dict)) # True

help(print)
help(isinstance)