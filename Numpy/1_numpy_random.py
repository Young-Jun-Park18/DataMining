import numpy as np

#np.random.seed(1) # np.random.seed(x) -> seed 괄호에 x를 다르게 하면 서로 다른 범위의 랜덤 값을 설정할 수 있다.


# random.~의 여러가지 기능들
print(np.random.rand(2,3)) # .rand(m,n) = 0~1 사이 균일분포 매트릭스 생성
print(np.random.randn(2,3)) # .randn(m,n) = 평균0, 표준편차1의 표준정규분포 매트릭스 생성
print(np.random.randint(1,20)) # .randint(m,n) = m~n-1 사이의 랜덤값을 생성

