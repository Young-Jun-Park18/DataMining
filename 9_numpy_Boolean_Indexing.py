# I : 넘파이 배열의 모든 원소를 == operator를 통해 true or false의 결과로 추출할 수 있다.

import numpy as np

names = np.array(["영준", "주은", "현희", "대현", "재희", "인택"])
data = np.random.randn(6, 4) # 6행 4열 랜덤값 생성
print(names)
print(data)

# ==을 통해 names라는 배열의 모든 원소와 비교하여 true or false 값을 도출
print(names == '영준')
print(data[names == "영준"]) # names의 true 값인 0행을 모두 가져옴
print(data[names == "영준", 2:]) # names의 0행 && 2열~끝까지 교집합을 출력