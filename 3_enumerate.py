# I : enumerate는 순서가 있는 자료형을 출력할 때 값과 인덱스까지 같이 출력해줍니다.
my_list = ['가', '나', '다']
print(my_list)                        # 리스트의 값만 나옴
print(list(enumerate(my_list)))       # 리스트의 값과 인덱스가 쌍을 이룸

