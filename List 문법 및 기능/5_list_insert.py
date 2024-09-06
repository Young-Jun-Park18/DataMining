# I : list.insert(삽입을 원하는 index, 삽입 내용)이 기본 문법이다.

# I : .append()와 다른 점은 append는 리스트 가장 끝에 원소를 추가하지만,
#     .insert()는 원하는 위치에 추가할 수 있다는 장점이 있다.

my_list = ['가', '나', '다', '라']
my_list.insert(1,0)
print(my_list)

# 주의할 점 _ 1
# .extend()와 마찬가지로 print(my_list.insert())를 하게 되면 None으로 나온다
# 따라서 insert()를 먼저해주고 그 다음 문장에 print(my_list)를 해주자

# I : insert와 for문을 사용해서 리스트를 복제할 수 있다.
my_list2 = []
for i in range(len(my_list)):
    my_list2.insert(i,my_list[i])
print(my_list2)

# 주의할 점 _ 2
# 복제하기 전에 미리 빈 리스트인 my_list2 = []를 만들어놓지 않으면
# not defined name error가 발생한다