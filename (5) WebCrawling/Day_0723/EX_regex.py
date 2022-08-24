# 모듈 로딩
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# for i in range(1, 54):
#     address = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=' + str(i) + '&sido=&gugun=&store='
#     html = urlopen(address)
#     bs = BeautifulSoup(html, "html.parser")
#     # 정보 불러오기
#     store_info = bs.find_all("td", "center_t")
#     # 필요한 데이터만 추출(인덱싱 사용)
#     for j in range(0, len(store_info), 6):
#         store_location_list.append(store_info[j].text)
#         store_name_list.append(store_info[j+1].text)
#         store_address_list.append(store_info[j+3].text)
#         store_tell_list.append(store_info[j+5].text)

# 할리스 매장 1페이지
# https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1&sido=&gugun=&store=
# 페이지 소스 분석 => 찾고자 하는 정보가 td 라는 id 하위에 있는 정보임

address_list= []
tel_list = []
store_list = []
city_list = []

# 페이지 리딩
for i in range(1, 54):
    address = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=' + str(i) + '&sido=&gugun=&store='
    page_open = urlopen(address)
    page_read = BeautifulSoup(page_open, 'html.parser')

    # id = td인 정보 분리
    filter_tel = re.compile('^\d{2,}-\d{2,}-\d{2,}$|^\.|없음|x$|^\d{2,}-\d{2,}$|^\d{2,}\)\d{2,}-\d{2,}$')
    filter_city = re.compile('[시|군|구]$')
    filter_store = re.compile('[점]$')
    filter_address = re.compile('[시|군|구|도]\s.+\s.+\s.')
    find_tel = page_read.find_all('td', text=filter_tel)
    find_city = page_read.find_all('td', text=filter_city)
    find_store = page_read.find_all('td', text=filter_store)
    find_address = page_read.find_all('td', text=filter_address)
    for j in range(0, len(find_tel)):
        # address_list.append(find_address[j].text)
        # store_list.append(find_store[j].text)
        tel_list.append(find_tel[j].text)
        # city_list.append(find_city[j].text)

print(len(tel_list))
# # 판다스 DF객체 생성
# coffeeDF = pd.DataFrame({'지역': city_list,
#                          '매장명': store_list,
#                          '주소': address_list,
#                          '전화번호': tel_list})
#
# # csv파일로 저장
# coffeeDF.to_csv('hollys_branches_임재원.csv', encoding='cp949')


