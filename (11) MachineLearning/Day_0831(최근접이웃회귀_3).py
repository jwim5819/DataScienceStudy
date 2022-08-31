import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

# 데이터 준비
df = pd.read_csv('https://bit.ly/perch_csv')
perch_full = df.to_numpy()  # DataFrame을 Numpy의 array로 변환
print(perch_full[:5])
print(perch_full.shape)

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
)

train_input, test_input, train_target, test_target = train_test_split(
    perch_full, perch_weight, random_state=42)

poly = PolynomialFeatures(include_bias=False)
poly.fit(train_input)
train_poly = poly.transform(train_input)  # train_input 데이터를 이용하여

# 총 9개의 특성이 만들어짐
print(train_poly[0:3])
print(train_poly.shape)
test_poly = poly.transform(test_input)  # 테스트 세트 변환: fit()호출 안함

print(poly.get_feature_names())

# 다중 회귀 모델 훈련 =============================================
lr = LinearRegression()
lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))

# 고차항의 최대 차수 증가 (5차)
poly = PolynomialFeatures(degree=5, include_bias=False)
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)
print(train_poly.shape)

# 선형 회귀 모델 훈련 및 훈련 세트 점수 계산
lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target))
# 테스트 세트 점수 계산
print(lr.score(test_poly, test_target))  # 훈련 세트에 과대 적합

# 표준화
ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

# 릿지 회귀
ridge = Ridge()  # alpha=1.0
ridge.fit(train_scaled, train_target)
print(ridge.score(train_scaled, train_target))  # 훈련 세트 점수 확인
print(ridge.score(test_scaled, test_target))  # 훈련 세트의 점수가 정상화됨

# 릿지 회귀에서 적절한 alpha값 찾기
train_score = []
test_score = []
alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
    ridge = Ridge(alpha=alpha)
    ridge.fit(train_scaled, train_target)
    # 훈련 세트와 테스트 세트 점수를 저장
    train_score.append(ridge.score(train_scaled, train_target))
    test_score.append(ridge.score(test_scaled, test_target))
plt.plot(np.log10(alpha_list), train_score,
         label='train_set score', marker='o', markersize=3)
plt.plot(np.log10(alpha_list), test_score,
         label='test_set score', marker='s', markersize=3)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.legend()
plt.show()

# alpha=0.1 적용
ridge = Ridge(alpha=0.1)
ridge.fit(train_scaled, train_target)
print(ridge.score(train_scaled, train_target))
print(ridge.score(test_scaled, test_target))
