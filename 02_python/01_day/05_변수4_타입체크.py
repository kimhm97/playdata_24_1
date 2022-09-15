'''

    변수에 저장된 데이터의 종류 알아보기

'''
# 1. 기본형 데이터의 타입 알아보기
int_value = 10
float_value = 3.14
bool_value = True

def fun():
    pass

func_value = fun
none_value = None

print("int_value:", int_value, type(int_value))       # <class 'int'>
print("float_value:", float_value, type(float_value)) # <class 'float'>
print("bool_value:", bool_value, type(bool_value))    # <class 'bool'>
print("func_value:", func_value, type(func_value))    # <class 'function'>
print("none_value:", none_value, type(none_value))    # <class 'NoneType'>

# 2.  집합형
str_value = "Hello"
list_value = [10,20]
tuple_value = (10,20)
set_value = {10, 20}
dict_value ={"name":"홍길동","age":20}

print("str_value:", str_value, type(str_value))          # <class 'str'>
print("list_value:", list_value, type(list_value))       # <class 'list'>
print("tuple_value:", tuple_value, type(tuple_value))    # <class 'tuple'>
print("set_value:", set_value, type(set_value))          # <class 'set'>
print("dict_value:", dict_value, type(dict_value))       # <class 'dict'>



