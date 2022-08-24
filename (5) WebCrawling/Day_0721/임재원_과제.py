from urllib.request import urlopen
from bs4 import BeautifulSoup


# 함수 생성
def parse_use_find(html):
    '''
    기후 정보 분석 : find()함수 사용
    :param html : 웹사이트 전체 html
    :return:
    '''
    # 디버깅 키 => F8 : 한라인씩 실행(step over), F7 : 함수 내부로 이동(step into)
    seven_day = html.find('div', id='seven-day-forecast')
    # print(seven_day)
    forecast_items = seven_day.find_all('div', class_='tombstone-container')
    # print(len(forecast_items))
    for day in forecast_items:
        if day.find(class_='temp') is not None:   # class='temp'가 있는 경우에만 찾겠다.
            period = day.find('p', class_='period-name').text
            short_desc = day.find('p', class_='short-desc').text
            temp = day.find('p', class_='temp').text
            image_desc = day.find('img')['title']
            print('-='*50)
            print(f'[period] = {period}')
            print(f'[temp] = {temp}')
            print(f'[short_desc] = {short_desc}')
            print(f'[image_desc] = {image_desc}')


def parse_use_select(html):
    '''
    기후 정보 분석 :  select()함수 사용
    :param html : 웹사이트 전체 html
    :return:
    '''
    pass


page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
html = BeautifulSoup(page.read(), 'html.parser')

parse_use_find(html)
parse_use_select(html)