# 기본적으로 숫자는 오름차순, 문자는 대문자 A ~ 소문자 z 순서로 정렬됩니다.
my_list = [5, 2, 1, 7, 8]
my_list2 = ['C' , 'B', 'a', 'Z', 'd', 'e',]
my_list.sort()
my_list2.sort()
print(my_list)
print(my_list2)

# .sort( reverse = True ) 를 사용해서 역으로 정렬할 수 있습니다.
my_list.sort(reverse = True)
my_list2.sort(reverse = True)
print(my_list)
print(my_list2)

# .sort( key = len ) 을 통해 문자 길이를 기준으로 정렬할 수 있습니다.
my_list3 = ['name', 'hi', 'youngjun']
my_list3.sort(key = len)
print(my_list3)
my_list3.sort(reverse = True)
print(my_list3)