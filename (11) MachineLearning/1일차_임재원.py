import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# 데이터
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

# train 그룹 생성
fish_data = np.column_stack((fish_length, fish_weight))
domi = np.ones(35)
smelt = np.zeros(14)
fish_target = np.concatenate((domi, smelt))
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)
np.random.seed(42)
index_list = np.arange(49)
train_input = input_arr[index_list[:]]
train_target = target_arr[index_list[:]]

# neighbors에 따른 score계산
score = []
neighbors = []
for i in range(5, 50):
    kn = KNeighborsClassifier(i)
    kn.fit(train_input, train_target)
    score.append(kn.score(train_input, train_target))
    neighbors.append(i)

# 플롯 그리기
plt.figure(figsize=(20, 10))
plt.plot(neighbors, score, 's-', ms=5)
plt.xlabel('neighbors')
plt.ylabel('score')
plt.xticks(neighbors, fontsize=9)
plt.yticks(score)
plt.show()

# 데이터 프레임 생성
df = np.column_stack((neighbors, score))
df = pd.DataFrame(df)
df.columns = ['neighbors', 'score']
print(df)
