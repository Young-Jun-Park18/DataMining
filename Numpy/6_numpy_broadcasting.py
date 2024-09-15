# I : 넘파이 배열_np.array([]) 의 좋은 점은 for문을 사용하지 않고 데이터를 일괄 처리 가능하다

import numpy as np

sample_arr1 = np.array([[1,2,3],[4,5,6]])
print(sample_arr1)

sample_arr1 = sample_arr1 + sample_arr1 # 각 배열에서 같은 index 끼리 연산 (사칙연산 모두 가능)
print(sample_arr1)

# I : 넘파이 배열끼리 크기 비교를 할 수 있고 boolean type으로 출력된다
sample_arr2 = np.array([[2.4, 2.1, 2.9],[3.9, 5.1, 5.8]])
print(sample_arr1 > sample_arr2)