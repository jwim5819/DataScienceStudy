import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
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

train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42)

train_input = train_input.reshape(-1, 1)  # 2차원 배열로 변경
test_input = test_input.reshape(-1, 1)  # 2차원 배열로 변경

lr = LinearRegression()
# 선형 회귀 모델 훈련
lr.fit(train_input, train_target)
# 50cm 농어에 대한 예측
print('50cm: ', lr.predict([[50]]))
# 기울기(a): coef_, 절편(bias): intercept_
print(lr.coef_, lr.intercept_)

plt.scatter(train_input, train_target)
# 15에서 50까지 1차 방정식 그래프 그리기
# plot([x축 데이터:시작, 끝], [y축 데이터:시작, 끝])
plt.plot([15, 50], [15 * lr.coef_ + lr.intercept_, 50 * lr.coef_ + lr.intercept_],
         color='red', linestyle='--')
# 50cm 농어 데이터
plt.scatter(50, 1241.8, marker='^', color='orangered')
plt.show()

print('train data score: ',
      lr.score(train_input, train_target))
print('test data score: ',
      lr.score(test_input, test_target))

# 다항 회귀식 구하기 =====================================
# 훈련세트에 데이터 추가
train_poly = np.column_stack((train_input ** 2, train_input))
test_poly = np.column_stack((test_input ** 2, test_input))
print(train_poly[0:5])
print(train_poly.shape, test_poly.shape)

# 제곱한 데이터를 이용하여 선형 회귀 모델을 다시 훈련
lr = LinearRegression()
lr.fit(train_poly, train_target)
print(lr.predict([[50 ** 2, 50]]))  # 50cm 농어의 무게 예측
print(lr.coef_, lr.intercept_)

# 구간별 직선을 그리기 위해 15에서 49까지 정수 배열을 만듬
point = np.arange(15, 50)
# 훈련 세트의 산점도 그리기
plt.scatter(train_input, train_target)
# 15에서 49까지 2차 방정식 그래프 그리기
plt.plot(point, 1.01 * point ** 2 - 21.6 * point + 116.05,
         color='red', linestyle='--')
# 50cm 농어 데이터(무게:1574g)
plt.scatter([50], [1574], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))
