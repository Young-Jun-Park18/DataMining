# I : numpy에서 제공하는 np.round() 함수는 반올림을 해주는 함수입니다.
import numpy as np

data = np.random.randn(2,3)
data2 = np.round(np.random.randn(2,3))
print(data)
print(data2)

# I : numpy에서는 리스트 + 리스트도 가능하고 리스트 * 정수도 가능하다
print(data2 * 10) # 브로드캐스팅
print(data + data2) # 브로드캐스팅