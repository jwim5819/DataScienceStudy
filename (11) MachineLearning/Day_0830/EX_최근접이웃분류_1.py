import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()

bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0,
                33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0,
                41.0]

bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0,
                600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0,
                1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]

smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 도미 산점도
plt.scatter(bream_length, bream_weight)
plt.xlabel('Bream Length')
plt.ylabel('Bream Weight')
plt.show()

# 도비, 빙어 산점도
plt.scatter(bream_length, bream_weight, label='bream')
plt.scatter(smelt_length, smelt_weight, label='smelt')
plt.xlabel('length')
plt.ylabel('weight')
plt.legend()
plt.show()

# 도미, 빙어 데이터 합치기
length = bream_length + smelt_length
weight = bream_weight + smelt_weight

# 1차원 데이터를 2차원으로 변경
fish_data = [[length, weight] for length, weight in zip(length, weight)]
print(fish_data)

# 정답 데이터(fish target) 준비 / 찾고자 하는 데이터인 도미를 1로 설정
fish_target = [1] * 35 + [0] * 14
print(fish_target)

# fish_data와 fish_target을 활용하여 모델 훈련
kn.fit(fish_data, fish_target)

# 정확도의 평균값으로 모델 평가
score = kn.score(fish_data, fish_target)
print(f'score : {score}')

# 새로운 데이터를 활용한 결과 예측 / class label 리턴(0, 1)
predict = kn.predict([[30, 600]])
print(f'predict : {predict}')

plt.rc('font', family='Malgun Gothic')
plt.scatter(bream_length, bream_weight, label='bream(도미)')
plt.scatter(smelt_length, smelt_weight, label='smelt(빙어)')
plt.scatter(30, 600, marker='^', color='red')
plt.xlabel('length')
plt.ylabel('weight')
plt.legend()
plt.show()
