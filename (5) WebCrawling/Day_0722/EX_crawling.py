from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, "html.parser")
# find_all() => list 형태로 값을 return 해준다
nameList = bs.find_all('span', {'class': 'green'})    # 녹색 부분만 찾는다.(사람 이름)
print(len(nameList))

for name in nameList:
    print(name.get_text())

# 특정 단어 찾기(검색어 사용)
princeList = bs.find_all(text='the prince')
print(princeList)
print(f'the prince count : {len(princeList)}')

# 트리 이동 => 문서 내부에서 특정 위치를 기준으로 태그 찾을 때
#         => 단방향으로 트리 이동
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
table_tag = bs.find('table', {'id': 'giftList'})

for child in table_tag.children:
    print(child)

desc = bs.find('table', {'id': 'giftList'}).descendants
print(f'descendants 갯수: {len(list(desc))}')

for child in bs.find('table', {'id': 'giftList'}).descendants:
    print(child)

for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)

for sibling in bs.find('table', {'id': 'giftList'}).previous_sibling:
    print(sibling)

# 문자열 마지막에 whitespace가 있는 경우(\n, \r등)
# 해당 whitespace를 next_sibling으로 반환한다
sibling1 = bs.find('tr', {'id': 'gift3'}).next_sibling
print(ord(sibling1))  # ord(문자): 문자의 Unicode 정수를 리턴

# next_sibling.next_sibling 이용
sibling2 = bs.find('tr', {'id': 'gift3'}).next_sibling.next_sibling
print(sibling2)  # ord(문자): 문자의 Unicode 정수를 리턴

# 부모 다루기 (parnet => 나를 감싸고 있는 상위 tag)
# .parent 사용
style_tag = bs.style
print(style_tag.parent)

img1 = bs.find('img', {'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)