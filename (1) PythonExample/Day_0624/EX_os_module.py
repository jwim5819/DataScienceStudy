# ===================================================================
# file, dir 관련된 모듈
# ===================================================================
import os.path as path
import os
# ===================================================================
# 특정 폴더 존재 여부 체크하고 해당하는 폴더가 없으면 폴더를 생성
# ===================================================================
DIR_PATH = r'./DATA'
DIR_PATH2 = r'./image/jpg/01'
if not path.exists(DIR_PATH):
    os.mkdir(DIR_PATH)      # 하나의 폴더만 생성할 때
if not path.exists(DIR_PATH2):
    os.makedirs(DIR_PATH2)      # 하위 폴더까지 생성하고 싶을 때
DATA_file = DIR_PATH2 + r'/flower.jpg'
if not path.exists(DATA_file):      # 폴더 뿐 아니라 파일도 검사가능함.
    print(f'파일없음.')
# ===================================================================
# 폴더 안의 특정 경로에 존재하는 내용 리스트 화
# ===================================================================
data_list = os.listdir(r'./address_book')
print(f'{data_list}')
# ===================================================================
# 시간 관련 모듈
# ===================================================================
import time as t
print(t.time())
print(t.localtime(t.time()))
current_time = t.localtime(t.time())
print(f'현재 년도 {current_time.tm_year}년')
print(f'현재 날짜 {current_time.tm_mday}일')
print(f'현재 시간 {current_time.tm_hour}시')
print(t.strftime('%A %B %H', t.localtime(t.time())))

for num in range(30):
    print(f'■', end='')
    t.sleep(0.1)