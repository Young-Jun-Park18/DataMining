import numpy as np

# I : np.dtype을 통해 현재 array의 데이터 타입을 확인할 수 있다.
sample_arr1 = np.array([1, 2, 3, 4, 5])
sample_arr2 = np.array([1, 2.6, 3, 0.9])
print(sample_arr1.dtype)
print(sample_arr2.dtype)

# 주의할 점 : 일반 파이썬 기본 리스트[]에는 list.dtype을 사용할 수 없다.
#           오직 넘파이 배열을 사용한 np.array([])로 만든 것에만 dtype을 사용할 수 있다.
#           일반 파이썬 기본 리스트는 다양한 데이터 타입을 저장할 수 있지만,
#           넘파이 배열의 모든 요소는 동일한 데이터 타입을 가져야 한다.



# I : ndarray.astype = (np.float64) 를 통해 ndarray의 타입을 강제로 float 타입으로 변경할 수 있다.
sample_arr3 = np.array([1.0, 2, 3, 4, 5])
print(sample_arr3.dtype)
sample_arr3 = sample_arr3.astype(np.int64)
print(sample_arr3.dtype)

# 주의할 점 : 요소들이 어떤 건 정수고, 어떤 건 실수로 섞여 있을 때 astype을 사용할 수 있다.
#           실수를 정수로 바꾼다면 소수점 뒤에는 버림 연산을 한다.

# I : astype을 사용하기 귀찮다면 넘파이 배열을 선언할 때 뒤에 , dtype = int64로 데이터 타입을 설정할 수 있다.
sample_arr4 = np.array([.22, .370, .44, 4, 5], dtype = np.float64)
print(sample_arr4.dtype)