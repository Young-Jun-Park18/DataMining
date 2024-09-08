# I : 튜플은 소괄호()로 작성합니다.
# I : 인덱스가 1개인 튜플은 string으로 인식될 수 있기에 콤마를 꼭 붙인다. tuple = ('가',)
# I : 튜플은 항목의 추가, 삭제, 수정이 불가능합니다.

my_tuple = ('사과', '딸기', '바나나')
my_tuple2 = ('red',) # type = tuple
my_tuple3 = ('red') # type = str
print(type(my_tuple2))
print(type(my_tuple3))

# I : 튜플에 접근할 때에도 대괄호를 사용합니다.
print(my_tuple[2])

# I : 튜플은 데이터의 변동이 없기 때문에 안정적인 데이터 보관이 가능하고
#     딕셔너리의 키로 사용이 가능합니다.