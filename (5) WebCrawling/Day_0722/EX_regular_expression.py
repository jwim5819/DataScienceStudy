# 정규 표현식(regex) => 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식언어
# 문자열의 치환, 검색, 추출 / 문자열의 유효성 검사
# 정규 표현식 기호는 강의 PDF참고
import re

# compile() 사용 안함
# match(pattern, 문자열)
m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!'))
print('-='*50)

# compile() 사용
# 정규식 객체 p 생성, 여러번 사용할 수 있음
# search() 메소드 => 일치하는 첫 번째 문자열만 리턴
p = re.compile('[a-z]+')    # 알파벳 소문자
m = p.match('python')
print(m)
print(p.search('I like apple 123'))
print(p.search('I like apple 123').group(0))    # groups(), group(0): 매친되는 전체 문자열 리턴
print('-='*50)

# findall() 메소드 => 일치하는 모든 문자열을 리스트로 리턴
p = re.compile('[a-z]+')
print(p.findall('Life is too short!'))
print(p.findall('Life is too short!')[2])    # 리스트 형태이기 때문에 요소로 빼올수도 있다
print('-='*50)

# match() 메소드 => 전화번호 분석 (지역번호-국번-전화번호)
# (2, 3자리)-(3, 4자리)-(4자리)
tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')

print(tel_checker.match('02-123-4567'))
print(tel_checker.match('053-950-45678'))
print(tel_checker.match('053950-4567'))
print('-='*50)

# groups() 메소드 => 매칭 결과를 튜플로 출력
m = tel_checker.match('02-123-4567')
print(m.groups())    # group(0) => 02-123-4567
print(m.group(1))    # group(1) => (1)(2) (3)
print(m.group(2, 3))
print(f'시작인덱스 : {m.start()}, 끝 인덱스(+1) : {m.end()}')
print('-='*50)

# 전방 탐색(lookahead)
# 전방 긍정 탐색 => 패턴과 일치하는 문자열을 만나면 패턴 앞의 문자열 반환
# (?=패턴)
lookahead1 = re.search('.+(?=won)', '1000 won')
print(f'전방 긍정 탐색 : {lookahead1}')
lookahead2 = re.search('.+(?=log:)', '2022-07-01 00:00:01 ABC.log: 전방탐색')
print(f'전방 긍정 탐색 : {lookahead2}')

# 전방 부정 탐색 => 패턴과 일치하지 않는 문자열을 만나면 해당 문자열 반환
# (?!패턴)
lookahead3 = re.search('\d{4}(?!-)', '010-1234-5678')
print(f'전방 부정 탐색 : {lookahead3}')
print('-='*50)

# 후방 탐색(lookbehind)
# 후방 긍정 탐색 => 패턴과 일치하는 문자열을 만나면 패턴 뒤의 문자열 반환
# (?<=패턴)
lookbehind1 = re.search('(?<=log:).+', '2022-07-01 00:00:01 ABC.log: this is python')
print(f'후방 긍정 탐색 : {lookbehind1}')
lookbehind2 = re.search('(?<=:).+', 'USD: $51')
print(f'후방 긍정 탐색 : {lookbehind2}')

# 후방 부정 탐색 => 패턴과 일치하는 않는 문자열을 만나면 해당 문자열 반환
# (?<!패턴)
lookbehind3 = re.search('\\b(?<!\$)\\d+\\b', 'I paid $30 for 100 apples.')
print(f'후방 부정 탐색 : {lookbehind3}')
lookbehind4 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apples.')
print(f'후방 부정 탐색 : {lookbehind4}')
print('-='*50)

