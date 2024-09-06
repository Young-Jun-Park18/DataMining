# I : 리스트는 대괄호 [] 를 사용하고, 여러 타입을 같이 쓸 수 있다
my_list = [5, 20, 35, "mju"]
print(my_list[0])

# I : -2는 뒤에서 두번 째를 의미한다.
print(my_list[-2])

# I : 리스트는 값을 변경할 수 있다.
my_list[-3] = 60181889
print(my_list)

# I : 리스트는 덧셈 연산자 " + " 로 합칠 수 있고, 중복 허용.
# I : 넣은 순서대로 합쳐진다
ex_list1 = [0, 1, 2]
ex_list2 = [3, 4, 5]
print(ex_list1 + ex_list2)
print(ex_list2 + ex_list1)

# I : 리스트는 리스트끼리 더해야 한다.
print(ex_list1 + 4) # type error 발생