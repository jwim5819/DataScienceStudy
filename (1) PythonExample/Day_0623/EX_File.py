# Path -> 경로는 두가지가 있다. 절대경로, 상대경로
# 절대경로 : 파일 및 폴더가 존재하는 경로.
# 상대경로 : 현재 코드파일이 들어있는 폴더를 기준으로 경로를 지정.
#          . : 현재 위치 / .. : 상위 위치
# ===================================================================
file = r'./Html/Home.html'
# ===================================================================
# Home.html 파일을 라인 단위로 읽어서 화면에 출력하기
# ===================================================================
file = open(file, mode='r', encoding="UTF-8")
while True:
    line = file.readline()
    print(f'{line}', end='')
    if not line:
        break
file.close()
print(f'\n===============================================')
file = r'./Html/Home.html'
file = open(file, mode='r', encoding="UTF-8")
while True:
    line = file.readline()
    line = line.strip()
    print(f'{line}')
    if not line:
        break
file.close()
print(f'\n===============================================')
# ===================================================================
# with 파일 as 구문
# close()를 생략가능함.
# ===================================================================
file = r'./Html/Home.html'
with open(file, mode='r', encoding="UTF-8") as file:
    while True:
        line = file.readline()
        print(f'{line}', end='')
        if not line:
            break
