import random

# [과제1] Lst = [random.randint(1,100) for i in range(20)]

# (1-1)위 코드를 이용하여 Lst와 같은 리스트 2개를 생성하고, 두 리스트가 합쳐져 40개가 되도록하라
def combine():
    random_lst1 = [random.randint(1,100) for i in range(20)]  # 첫 번째 랜덤 리스트 생성
    random_lst2 = [random.randint(1,100) for i in range(20)]  # 두 번째 랜덤 리스트 생성
    combine_lst = random_lst1 + random_lst2                         # 두 리스트 합쳐서 40개로 만들기
    combine_lst.sort(reverse = False)                               # 가시성을 위해 오름차순으로 정렬
    print('두 개의 리스트를 합친 결과')
    print(combine_lst)                                              # 출력

# (1-2) 1번의 결과에 중복 없는 고유한 숫자만 출력하시오
    deduplication_lst = []                                          # 빈 리스트 생성
    for i in combine_lst:                                           # for문
        if i not in deduplication_lst:                              # 만약 빈 리스트에 i가 없다면
            deduplication_lst.append(i)                             # 추가
    print('중복을 제거한 리스트')
    print(deduplication_lst)                                        # 출력



# [과제2] 8명의 학생과 10개의 문제, 그리고 답은 2차원 리스트에 저장되어 있다 각 행은 문제에 대한 학생의 답을 저장하고 있을 때
#        시험 평가와 결과를 출력 하시오
def test():
    student_lst = []                                                # 8명의 학생과 10개의 문제를 담을 리스트 생성
    for i in range(8):                                              # 반복문
        row = []                                                    # 1줄의 빈 리스트 생성
        for j in range(10):                                         # 반복문
            row.append(random.randint(65,90))                 # 1명당 10개의 답을 작성하므로 A~Z의 아스키코드인 65~90을 10개 생성
        student_lst.append(row)                                     # 랜덤 아스키코드가 담긴 1줄을 student_lst에 추가
    print('질문에 대한 학생의 답')                                     # 학생의 답 80개 출력
    for row in student_lst:
        print(row)

    student_numbers = [i for i in range(0, 10)]                          # 학생 번호 1~10
    correct_answers = [random.randint(65, 90) for _ in range(10)]  # 정답 생성
    answer_lst = [student_numbers, correct_answers]                      # 질문에 대한 정답 리스트
    print('질문에 대한 정답')
    for i in range(2):
        print(answer_lst[i])

    for i in range(8):
        count = 0
        for j in range(10):
            if student_lst[i][j] == answer_lst[1][j]:                    # 학생 답안과 정답을 비교
                count += 1
        print(i, "번 학생의 정답 문항의 개수는" , count, "개 입니다.")



def main():                                                              # 메인 함수
    combine()
    test()

main()


# 과제를 하면서 해결하기 힘들었던 것

# 1 : count가 계속 증가하지 않고 0개 였는데,
#     row.append([random.randint(65, 90)]) 대신 row.append(random.randint(65, 90))로 바꿔서 해결.
#     학생들의 정답이 정수 형태가 아니라 리스트 형태라서 == 를 통해 비교할 때 계속 False 였던 것.

# 2 : 정수끼리 비교를 해서 출력까진 문제가 없었는데 이제 이 아스키코드를 어떻게 알파벳으로 바꿔야할지 고민했음.
#
