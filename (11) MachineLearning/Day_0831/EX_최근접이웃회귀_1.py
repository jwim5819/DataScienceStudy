import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

# 농어 데이터
perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0,
                         19.6, 20.0, 21.0, 21.0, 21.0, 21.3, 22.0, 22.0,
                         22.0, 22.0, 22.0, 22.5, 22.5, 22.7, 23.0, 23.5,
                         24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5,
                         27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
                         36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0,
                         40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5, 44.0])

perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0,
                         85.0, 85.0, 110.0, 115.0, 125.0, 130.0, 120.0,
                         120.0, 130.0, 135.0, 110.0, 130.0, 150.0, 145.0,
                         150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
                         218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0,
                         320.0, 514.0, 556.0, 840.0, 685.0, 700.0, 700.0,
                         690.0, 900.0, 650.0, 820.0, 850.0, 900.0,
                         1015.0, 820.0, 1100.0, 1000.0, 1100.0,
                         1000.0, 1000.0])

# 산점도 확인
plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 훈련 세트와 테스트 세트 준비
train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42)
print(f'train_input: {train_input}',
      f'test_input: {test_input}',
      sep='\n')

# reshape(-1, 1): -1: 행의 크기를 자동 지정
train_input = train_input.reshape(-1, 1)  # 2차원 배열로 변경
test_input = test_input.reshape(-1, 1)  # 2차원 배열로 변경
print(f'train_input: {train_input}',
      f'test_input: {test_input}',
      sep='\n')

# k-최근접 이웃 회귀 알고리즘 정확도 계산
knreg = KNeighborsRegressor()

# 모델 훈련
knreg.fit(train_input, train_target)

# score(): 훈련 모델 점수 확인, 결정 계수(R square)를 리턴
print(f'train score: {knreg.score(train_input, train_target)}')
print(f'test score : {knreg.score(test_input, test_target)}')

# mean_absolute_error(MAE): 평균 절대 오차 구하기
# 테스트 세트에 대한 예측값 계산
test_prediction = knreg.predict(test_input)

# 테스트 세트에 대한 평균 절대 오차 계산
mae = mean_absolute_error(test_target, test_prediction)
print(f'MAE: {mae}')

# Under fitting 해결 방안 => 이웃의 개수 줄임
knreg.n_neighbors = 3
knreg.fit(train_input, train_target)
print(f'train score: {knreg.score(train_input, train_target)}')
print(f'test score : {knreg.score(test_input, test_target)}')

# 이웃의 수를 변경하면서, 농어의 길이를 5 ~ 45까지 변경하면서 무게 예측
# x:농어의 길이(5 ~ 45까지 범위 설정)
x = np.arange(5, 45).reshape(-1, 1)

# n=1, 5, 10일때 예측 결과 그래프
for n in [1, 5, 10, 20]:
    knreg.n_neighbors = n
    knreg.fit(train_input, train_target)
    # 지정한 범위 x(농어의 길이)에 대한 농어 무게 예측하기
    prediction = knreg.predict(x)
    # 훈련 세트와 예측 결과 그래프 그리기
    plt.scatter(train_input, train_target, label='train set')
    plt.plot(x, prediction, label='prediction', color='orange')
    plt.title('n_neighbors = {}'.format(n))
    plt.xlabel('length')
    plt.ylabel('weight')
    plt.show()

# k-최근접 이웃 알고리즙의 문제점
# 훈련 밖의 샘플 예측
knreg.n_neighbors = 3
print('50cm:', knreg.predict([[50]]))
print('100cm:', knreg.predict([[100]]))

# 50cm 농어의 이웃을 구함
distances_50, indexes_50 = knreg.kneighbors([[50]])
# 100cm 농어의 이웃을 구함
distances_100, indexes_100 = knreg.kneighbors([[100]])
# 훈련 세트의 산점도
plt.scatter(train_input, train_target, label='train set')
# 훈련 세트 중에서 50cm 농어의 이웃 데이터만 다시 그림
plt.scatter(train_input[indexes_50], train_target[indexes_50],
            marker='D', label='50cm neighbors')
# 50cm 농어 데이터
plt.scatter(50, 1033, marker='^', label='100cm')
# 훈련 세트 중에서 100cm 농어의 이웃 데이터만 다시 그림
plt.scatter(train_input[indexes_100], train_target[indexes_50],
            marker='P', label='100cm neighbors')
# 100cm 농어 데이터
plt.scatter(100, 1033, marker='s', label='100cm')
plt.xlim(0, 110)
plt.legend(loc=5)
plt.show()
