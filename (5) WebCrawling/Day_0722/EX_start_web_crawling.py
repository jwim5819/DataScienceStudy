# 임의의 위키 페이지에서 모든 링크 목록 가져오기
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Kevin Bacon 위키피디아에서 'a'태그를 가지는 것을 출력. 단, 'herf'속성을 가지는 것만.
html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
print(f'Kevin Bacom page link 수 : {len(bs.find_all("a"))}')

# 'bodyContent' id 안의 내용중에 /wiki/로 시작하는 링크만 필터링
body_content = bs.find('div', {'id': 'bodyContent'})

'''
^(정규식 시작) ~ $(정규식 끝)
(/wiki/): '/wiki/'를 포함
((?!:).)*: ':'콜론이 없는 문자열 및 임이의 문자가 0회 이상 반복되는 문자열 검색
'''
pattern = '^(/wiki/)((?!:).)*$'
count = 0
for link in body_content.find_all('a', href=re.compile(pattern)):
    if 'href' in link.attrs:
        print(link.attrs['href'])
        count += 1
print(f'"/wiki/"로 시작하는 링크 수 {count}')

# 같은 페이지를 크롤링 하지 않으면서 전체 사이트 데이터 수집 코드
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('this page is missing something! Continuing.')

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('/wiki/Kevin_Bacon')
