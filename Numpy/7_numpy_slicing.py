# I : np.array([]) or np.arange()로 생성한 넘파이 배열은 슬라이싱으로 부분 발췌 및 수정을 할 수 있다.

import numpy as np
arr = np.arange(10)
print(arr) # 모든 요소
print(arr[5]) # 5번 index만
print(arr[5:8]) # 5번 index ~ 8번 직전 index까지 = 5, 6, 7

# I : 이런 슬라이싱을 통해 배열의 값을 변경 가능
arr[5:8] = 12 # 5번 index ~ 8번 직전 index의 값을 12로 변경
print(arr)

# I : 슬라이싱을 통해 새로운 배열을 만들 수 있음
arr2 = arr[5:8]
print(arr2)

arr2[0] = 100000
print(arr2)
print(arr)

# 주의할 점 : 이처럼 슬라이싱으로 만들어진 새로운 배열의 값을 변경하면 같은 메모리 값을 가지고 있기 때문에
#           원본 배열에도 값에 변화가 생긴다. 이러면 곤란하기 때문에 deep copy를 해야한다.

# 슬라이싱으로 독립된 배열 복사하는 방법 .copy()
arr3 = np.arange(10)
arr4 = arr3[5:8].copy()  # 이렇게 슬라이싱 복사를 할 때 뒤에 .copy()를 붙여주면 깊은 복사가 된다.
arr4[0:2] = 1000
print(arr3)
print(arr4)





