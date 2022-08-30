import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7,
               31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5,
               34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0,
               38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 10.5, 10.6, 11.0, 11.2,
               11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0,
               475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0,
               575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0,
               920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 7.5, 7.0, 9.7, 9.8,
               8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 2차원 리스트[길이, 무게]
fish_data = [[length, weight] for length, weight in zip(fish_length, fish_weight)]

# target 값 생성
fish_target = [1] * 35 + [0] * 14

# 훈련 세트 생성(35개)
train_input = fish_data[:35]
train_target = fish_target[:35]

# 테스트 세트 생성(14개)
test_input = fish_data[35:]
test_target = fish_target[35:]

kn = KNeighborsClassifier()  # 객체 생성
kn = kn.fit(train_input, train_target)  # 모델 훈련
test_score = kn.score(test_input, test_target)  # 테스트 세트로 평가 (정확도 출력)
print(f'test_score: {test_score}')

# Numpy를 활용해 배열 섞기
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)
np.random.seed(99)
index_list = np.arange(49)  # 0~48까지 값을 가지는 배열 생성
np.random.shuffle(index_list)  # 배열 내용을 무작위로 섞음

# 훈련 세트 생성
train_input = input_arr[index_list[:35]]
train_target = target_arr[index_list[:35]]

# 테스트 세트 생성
test_input = input_arr[index_list[35:]]
test_target = target_arr[index_list[35:]]

# 훈련 데이터, 테스트 데이터 확인
plt.scatter(train_input[:, 0], train_input[:, 1], label='train set')
plt.scatter(test_input[:, 0], test_input[:, 1], label='test set')
plt.xlabel('length')
plt.ylabel('weight')
plt.legend()
plt.show()

# 무작위로 섞인 훈련 세트와 테스트 세트를 이용하여 k-최근접 이웃 모델 생성 및 훈련
kn = kn.fit(train_input, train_target)
print("score: ", kn.score(test_input, test_target))
print("predict:     ", kn.predict(test_input))
print("test_target: ", test_target)  # predict 결과값과 비교를 위해 출력

# But, 도미가 나와야하는데 빙어가 나옴. 즉, 문제점이 아직 있다.
print(f'Predict(길이 25cm, 무게 150g): {kn.predict([[25, 150.0]])}')

# Numpy를 활용한 데이터 전처리================================================

# column_stack을 사용하여 리스트를 일렬로 세운 다음 차례대로 연결
fish_data = np.column_stack((fish_length, fish_weight))
print(fish_data)

# 개수 n개 만큼 각각 1과 0으로 채운 배열 생성
domi = np.ones(35)
smelt = np.zeros(14)

# concatenate를 사용하여 배열을 서로 연결, 연결된 배열은 튜플로 전달됨
fish_target = np.concatenate((domi, smelt))
print(fish_target)

# sklearn을 활용하면 numpy써서 배열 만들고 할 필요 없음========================

# 사이킷런으로 훈련세드와 테스트세트 나누기(train_test_split)
train_input, test_input, train_target, test_target = train_test_split(
    fish_data, fish_target, stratify=fish_target, random_state=42
)
print(f'train_input.shape = {train_input.shape}',
      f'test_input.shape = {test_input.shape}', sep='\n')
print(f'train_target = {train_target}')
print(f'test_target  = {test_target}')

# k-최근접 모델 적용(train_test_split함수로 나눈 데이터 사용)
kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
print("score: ", kn.score(test_input, test_target))

# 25cm, 150g의 생선 분류수(수상한 도미) => 여전히 0으로 나온다.
print(kn.predict([[25, 150]]))

# 산점도로 시각화해보기
plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(25, 150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 가장 가까운 이웃과의 거리 계산(default값은 5이고 가장 가까운 5개의 이웃 찾음)
distances, indexes = kn.kneighbors([[25, 150]])
print(f'distances = {distances}')
print(f'indexes = {indexes}')

# 이웃 5개 산점도로 시각화
plt.scatter(train_input[:, 0], train_input[:, 1], label='train_data',
            color='b')
plt.scatter(25, 150, marker='^', color='orange', label='Unknown')
plt.scatter(train_input[indexes, 0], train_input[indexes, 1],
            marker='D', label='neighbors', color='r')
plt.xlabel('length')
plt.ylabel('weight')
plt.legend()
plt.show()

print(f'neighbors: {train_input[indexes]}')
print(f'target: {train_target[indexes]}')
