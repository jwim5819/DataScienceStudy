# 모듈 로딩
import pandas as pd

# DF객체 생성
coffeeDF = pd.read_csv('hollys_branches_임재원.csv', encoding='cp949', index_col=0)


# 검색된 도시의 매장 출력 함수 생성
def find_store(city):
    si, goo = city.split()
    result = coffeeDF[coffeeDF['주소'].str.contains(si) & coffeeDF['주소'].str.contains(goo)]
    address, tel = result['주소'].to_list(), result['전화번호'].to_list()
    print('-' * 90)
    if len(address) == 0:
        print(f'검색된 매장이 없습니다.')
    else:
        for i in range(len(address)):
            print(f'[{i+1 : 3}]: [{address[i]}, {tel[i]}]')
        print('-' * 90)
        print(f'검색된 매장 수: {len(address)}')


city = input('검색할 매장의 도시를 입력하세요: ')
find_store(city)
