# I : 리스트 이름 뒤에 .append(내용)을 사용하여 원소를 추가할 수 있다

# I : 리스트를 생성할 때에는 대괄호[]를 사용하지만
my_list = ['기존', '메세지', '입니다']
print(my_list)

# 리시트에 있는 기능들을 사용할 때에는 소괄호()임을 잊지 말자
my_list.append('추가된 메세지 입니다')
print(my_list)

# Q : append는 한번에 1개만 추가할 수 있다 여러개는 불가능한가?
# A : 가능하지만 .extend라는 새로운 개념을 익혀야한다.
# S : 문법은 list.extend([내용1, 내용2, 내용3, 내용4])이다.
my_list.extend(['extend로', '추가된', '메세지입니다'])
print(my_list)

# 주의할 점 _ 1
# print(my_list.extend(('extend로', '추가된', '메세지입니다')))
# 위 코드로 실행하면 None이 나오기 때문에 반드시 extend와 print는 2줄로 따로 작성핮자

# 주의할 점 _ 2
# my_list.extend(['extend로', '추가된', '메세지입니다'])
# my_list.extend(('extend로', '추가된', '메세지입니다'))
#위 두 코드의 차이점 : 대괄호[]는 리스트 소괄호()는 튜플이니 주의하자



