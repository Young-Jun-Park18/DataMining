# I : 내장함수 zip(리스트1, 리스트2, 리스트3)은 각 리스트의 동일 인덱스끼리 묶어준다
my_list1 = ['가', '나', '다']
my_list2 = ['0', '1', '2']
my_list3 = ['a', 'b', 'c']

zipped = zip(my_list1, my_list2, my_list3) #우선 zip()해주고, list()로 만들고 print()로 감싸기
print(list(zipped))