# 기본 문법 : list.pop(index번호)를 통해 리스트 내 원하는 index를 삭제할 수 있다

my_list = ['박', '영', '준']
my_list.pop(0)
print(my_list)

# 주의할 점 _ 1
# append와 extend는 print() 내부에 작성할 시 None이 출력되지만
# .pop()은 print() 내부에 작성할 시 삭제된 원소를 출력한다
# 따라서 삭제되고 남겨진 리스트를 보고 싶다면 .pop()을 먼저 하고 print() 해야 함

my_list2 = ['김', '주', '은']
print(my_list2.pop(0))
print(my_list2)

# I : .append()와 똑같이 -1을 사용할 경우 가장 끝에 원소를 지운다
my_list2.pop(-1)
print(my_list2)