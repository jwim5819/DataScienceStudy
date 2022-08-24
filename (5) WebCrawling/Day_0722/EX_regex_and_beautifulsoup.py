from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# 제품 이미지 표현 문자열만 추출
# img_tag = re.compile('\.\.\/img\/gifts/img.*\.jpg')
img_tag = re.compile('/img/gifts/img.*.jpg')    # ‘.*’ 임의의 한 문자 0회 이상
images = bs.find_all('img', {'src': img_tag})
for image in images:
    print(image, end='  =>  ')
    print(image['src'])
print('-='*50)

# 대소문자 구분없이 특정 단어 검색
# '[T|t]{1}he prince' => T또는 t가 1회
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

# 소문자만 검색 결과
prince_list = bs.find_all(text='the prince')
print(f'소문자만 찾은 결과 {len(prince_list)}회')
# 대소문자 구분 없이 => find_all() 안에 정규식 사용
prince_list2 = bs.find_all(text=re.compile('[T|t]{1}he prince'))
print(f'대소문자 구분 없이 찾은 결과 {len(prince_list2)}회')
print('-='*50)

# Tag 속성에 접근하기
# <img> 태그의 src속성값 가져오기 => src속성에 이미지 정보를 가지고 있음.
soup = BeautifulSoup('<img src=../img/gifts/img1.jpg>', 'html.parser')
img_tag = soup.img

print(f'img.tag    =>    {img_tag}')
print(f'img.tag.atter    =>    {img_tag.attrs}')
print(f'img.tag.atter["src"]    =>    {img_tag.attrs["src"]}')
