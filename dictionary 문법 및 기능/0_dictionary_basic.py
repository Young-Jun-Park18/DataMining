# I : 딕셔너리는 키와 값을 가지며, 숫자와 문자를 쓸 수 있다.
#     키는 중복이 불가는항고 값은 중복이 가능하다
#     데이터를 추가 또는 삭제할 때 키와 값 쌍으로 입력해줘야한다.
#     딕셔너리는 중괄호{ key1 : value1, key2 : value2}로 구분한다.

my_dictionary = {1 : '박영준', 2 : '김주은'}
print(my_dictionary)

# I : 딕셔너리에 항목을 추가하고 싶다면
#     dictionary이름[key값] = value 값을 입력해준다.
my_dictionary[3] = '박현희'
print(my_dictionary)

# I : 딕셔너리에 항목을 제거하고 싶다면 del[key값]을 입력하면 된다
del my_dictionary[2]
print(my_dictionary)

