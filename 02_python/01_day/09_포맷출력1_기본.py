'''

    포맷출력

   예> 이름: 홍길동, 나이:20, 주소: 서울
       이름: 이순신, 나이:30, 주소: 부산

   1. "".format() 함수
  
'''
print(dir(str))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', 
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 

'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
'title', 'translate', 'upper', 'zfill']
'''
print(dir(int))
'''
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', 
'__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', 
'__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', 
'__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', 
'__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', 
'__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', 
'__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', 
'__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 
'__trunc__', '__xor__', 

'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 
'numerator', 'real', 'to_bytes']
'''
print(dir(float))
'''
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', 
'__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
'__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', 
'__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', 
'__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', 
'__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', 
'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 
'as_integer_ratio', 
'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
'''
print(dir(bool))
'''
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', 
'__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', 
'__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', 
'__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', 
'__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', 
'__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', 
'__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', 
'__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 
'__trunc__', '__xor__', 

'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 
'imag', 'numerator', 'real', 'to_bytes']
'''

print(dir(list))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', 
'__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
'__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 

'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 
'pop', 'remove', 'reverse', 'sort']
'''
print(dir(tuple)) # immutable 한 특징 때문에 수정 가능한 함수 제공 안됨.
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
 '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',

 'count', 'index']

print(dir(set))
'''
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', 
'__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', 
'__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', 
'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 

'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 
'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 
'union', 'update']
'''
print(dir(dict))
'''
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 

'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'''