# I : ndarray에는 5가지 속성이 있습니다.
# I : np.shape / np.ndim / np.dtype / np.size / np.itemsize

import numpy as np

data = np.random.rand(3,6)
print(data)

# np.shape는 행과 열 크기를 출력
print(data.shape) # (3행, 6열)

# np.ndim은 배열의 차원을 출력
print(data.ndim) # x축과 y축이 있는 2차원

# np.dtype은 데이터의 타입을 출력
print(data.dtype)

# np.size는 array의 원소 갯수를 출력해줍니다.
print(data.size)
