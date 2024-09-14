# I : ndarray을 생성하는 쉬운 방법은 np.array(리스트명)을 쓰는 것이다.

import numpy as np

sample_list = [1.5, 3, 4.5, 6]
ndarray = np.array(sample_list)
print(ndarray)

# I : 특수한 배열을 만드는 방법은 3가지가 있다. np.zeros(크기) / np.ones(크기) / np.empty(크기)

# np.zeros(size) = size만큼 0으로 채운 배열 생성
data1 = np.zeros((3, 6))
print(data1)

# np.ones(size) = size만큼 1으로 채운 배열 생성
data2 = np.ones((3, 6))
print(data2)

# np.empty(size) = size만큼 비어있는 배열 생성 (dummy 값이 들어있음 )
data3 = np.empty((1,3))
print(data3)

# np.arange(size) = 0~size만큼의 1차원 배열 생성
data4 = np.arange(5)
print(data4)


