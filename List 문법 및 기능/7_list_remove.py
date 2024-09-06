# 기본 문법 : list.remove(지우고 싶은 것)

# I : .pop()은 index를 지우는 것이라면, .remove()는 값을 지우는 것입니다.

my_list = [5, 4, 3, 2, 1, 0]
my_list.pop(0) # 0번 index에 존재하는 정수 5가 삭제됨.
print(my_list)

my_list.remove(0) # 리스트 내에 정수 0이 삭제됨.
print(my_list)

# Q : 만약 같은 숫자가 여러 개 있다면 어떻게 될까?
# A : 순차탐색이므로 리스트의 가장 앞에 있는 것만 삭제된다.
my_list2 = [0, 1, 2, 0, 1, 2]
my_list2.remove(0)
print(my_list2)

# S : 리스트 내 모든 0을 삭제하려면 while문을 사용하자
while 0 in my_list2:
    my_list2.remove(0)
print(my_list2)