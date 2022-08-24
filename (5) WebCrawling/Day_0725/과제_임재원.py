# 모듈 로딩
from bs4 import BeautifulSoup
import requests
import re

# 시가 총액 상위 10개 기업 가져올 url
html = requests.get('https://finance.naver.com/sise/sise_market_sum.naver')
soup = BeautifulSoup(html.text, 'html.parser')
# 'tr' [7] ~ [19] 인덱스가 1~10위 까지임.
# 단, [12~14]번 인덱스는 제외
read = soup.find_all('tr')

# 크롤링 결과를 담을 리스트 생성
stock_name_list = []
code_list = []
current_price_list = []
old_price_list = []
market_price_list = []
high_price_list = []
low_price_list = []
url_list = []


# 숫자만 추출해주는 함수 생성
def to_number(string):
    return re.sub(r'\d', '', string)


# 크롤링 함수 생성
def stock_crawling():
    for i in range(7, 20):
        if (i >= 12) and (i <= 14):
            pass
        else:
            goto_url = read[i].find('a')['href']   # 주식 페이지로 이동(상대 경로)
            new_url = 'https://finance.naver.com/' + goto_url
            url_list.append(new_url)
            html = requests.get(new_url)
            soup = BeautifulSoup(html.text, 'html.parser')
            process_1 = soup.find('div', class_='wrap_company')
            process_2 = soup.find('dl', class_='blind')
            process_3 = process_2.find_all('dd')
            stock_name_list.append(process_1.find('h2').text)    # 종목명
            code_list.append(process_1.find('span', class_='code').text)  # 종목코드
            current_price_list.append(process_3[3].text.split()[1])    # 현재가
            old_price_list.append(process_3[4].text.split()[1])    # 전일가
            market_price_list.append(process_3[5].text.split()[1])     # 시가
            high_price_list.append(process_3[6].text.split()[1])   # 고가
            low_price_list.append(process_3[8].text.split()[1])    # 저가


# print 및 input 함수 생성
def print_input():
    stock_crawling()
    print('-'*32)
    print(f'[ 네이버 코스피 상위 10대 기업 목록 ]')
    print('-'*32)
    for i in range(len(stock_name_list)):
        print(f'[{i+1:3}] {stock_name_list[i]}')
    while True:
        try:
            stock_number = int(input(f'주가를 검색할 기업의 번호를 입력하세요(-1: 종료): '))
            if stock_number == -1:
                break
            elif 1 <= stock_number <= 10:
                print(f'{url_list[stock_number-1]}')
                print(f'종목명: {stock_name_list[stock_number-1]}')
                print(f'종목코드: {code_list[stock_number-1]}')
                print(f'현재가: {current_price_list[stock_number-1]}')
                print(f'전일가: {old_price_list[stock_number-1]}')
                print(f'시가: {market_price_list[stock_number-1]}')
                print(f'고가: {high_price_list[stock_number-1]}')
                print(f'저가: {low_price_list[stock_number-1]}')
            else:
                print(f'잘못된 입력입니다.')
        except:
            print(f'잘못된 입력입니다.')

print_input()
