def main():
    name = get_name()
    print('hello', name)

def get_name():
   # name = input('What is your name? : ') 틀린 방식
   return input('What is your name? ') # 옳은 방식


main()

# Q : 위의 코드는 왜 오류가 날까?
# A : get_name(): 함수에서 정한 변수 name은 오직 get_name 내부에서만 살아있다
# S : get_name(): 함수에서 name을 선언하지 말고, return을 해준다.
