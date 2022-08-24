# 모듈 로딩
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# 리스트 생성
store_location_list = []
store_name_list = []
store_address_list = []
store_tell_list = []

# 웹 크롤링
for i in range(1, 54):
    address = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=' + str(i) + '&sido=&gugun=&store='
    html = urlopen(address)
    bs = BeautifulSoup(html, "html.parser")
    # 정보 불러오기
    store_info = bs.find_all("td", "center_t")
    # 필요한 데이터만 추출(인덱싱 사용)
    for j in range(0, len(store_info), 6):
        store_location_list.append(store_info[j].text)
        store_name_list.append(store_info[j+1].text)
        store_address_list.append(store_info[j+3].text)
        store_tell_list.append(store_info[j+5].text)

# 크롤링 결과 print
for i in range(len(store_location_list)):
    print(f'[{i+1}]: 매장이름: {store_name_list[i]}, 지역: {store_location_list[i]}, '
          f'주소: {store_address_list[i]}, 전화번호: {store_tell_list[i]}')
print(f'전체 매장 수: {len(store_location_list)}')

# 판다스 DF객체 생성
coffeeDF = pd.DataFrame({'지역': store_location_list,
                         '매장명': store_name_list,
                         '주소': store_address_list,
                         '전화번호': store_tell_list})

# csv파일로 저장
coffeeDF.to_csv('hollys_branches_임재원.csv', encoding='cp949')
