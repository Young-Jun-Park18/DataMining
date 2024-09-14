# I : numpy는 import numpy as "별명"으로 라이브러리를 추가할 수 있습니다.
# I : numpy는 순수 파이썬 코드로 작성한 반복문보다 10~100배 빠르고, 메모리도 적게 사용함
# I : numpy는 브로드캐스팅이 가능한 다차원 배열 ndarray를 제공합니다.
# I : numpy는 선형대수, 난수 생성기, 푸리에 변환 기능을 사용할 수 있다.
# I : numpy는 벡터 배열 상 데이터의 가공, 정제, 변형, 연산에 용이하다.
# I : 데이터분석에서는 정렬, 병합, 원소 찾기, 집합 연산, 데이터 수집 요약이 중요하다.

import numpy as np

# nparray VS python
np_array = np.arange(10)
py_array = list(range(10))

for _ in range(10): np_array = np_array * 2 # _ 언더바는 굳이 반복문에 변수 i가 필요 없을 때, 단순 반복만 할 때 사용해요
for _ in range(10): py_array = [x*2 for x in py_array] # 이런 for문 작성법은 리스트 컴프리헨션이다. [append값 for x in list if 조건]
# 결국 array에 *2하는 과정을 10번 반복하겠다는 뜻

print(np_array)
print(py_array)
# 둘 다 결과값은 같지만 ndarray가 훨~씬 빠르다


