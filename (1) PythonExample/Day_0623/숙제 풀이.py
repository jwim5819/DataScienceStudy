# =======================================================================
# PROGRAM = AddressBook_app
# DISCRIPTION = 파일 입출력, 문자열 데이터 처리, 함수 처리
# 조건 1. addressbook 이라는 개인 파일이 저장 되는 폴더를 생성할 것(이름_전화번호.txt)
#     2. 검색, 전체 보기, 추가, 종료 기능을 메뉴로 구현 할 것
#     3. 사용자가 종료 입력 전까지 무한 반복을 할 것.
# =======================================================================
# 전역 변수 및 상수(변경이 안되기 때문에 보통 대문자로 표시함)
DIR_PATH = r'./address_book/'       # 파일 저장 폴더
ADDR_LIST = []      # 주소 파일 저장 리스트
# =======================================================================
# 함수 정의
# =======================================================================
# 메뉴 출력 함수
# 함수명 : display_menu
# 파라미터 : 없음
# 반환값 : 없음
def display_menu():
    print(f'========나의 주소록========')
    print(f'{"1. 전체보기 : 1번":^22}')
    print(f'{"2. 검   색 : 2번":^23}')
    print(f'{"3. 추   가 : 3번":^23}')
    print(f'{"4. 종   료 : 4번":^23}')
    print(f'=========================')
# 전체 파일 이름 리스트 출력 함수
# 함수명 : display_file_name
# 파라미터 : 없음
# 반환값 : 없음
def display_file_name():
    print(f'<현재 등록된 주소록>')
    for addr in ADDR_LIST:
        print(f'{addr}')
# 어드레스 리스트의 주소록 검색 및 정보출력 함수
# 함수명 : search_addr
# 파라미터 : 이름, 전화번호 등의 str 데이터
# 반환값 : 없음
def search_addr(word):
    # 파일명 리스트 안에서 검색어의 존재 여부 확인
    for addr in ADDR_LIST:
        if word in addr:
            print(f'파일명 : {addr}')
            with open(DIR_PATH+addr+'.txt', mode='r', encoding='utf-8') as f:
                print(f'정 보 : {f.read()}')
# 주소록 파일 생성 및 추가 함수
# 함수명 : add_addr
# 파라미터 : 이름, 전화번호, 지역, 이메일 or 없음
# 반환값 : 없음
def add_addr(name, phone, location):
    file_name = name + '_' + phone + '.txt'
    # 파일명 리스트 추가
    ADDR_LIST.append(file_name[:-4])
    # 폴더에 파일 생성
    with open(DIR_PATH+file_name, mode='w', encoding='utf-8') as f:
        f.write(name+','+phone+','+location)
# 프로그램 초기화 함수(address_book 안에 존재하는 파일을 addr_list에 추가)
# 함수명 : clean_app
# 파라미터 : 없음
# 반환값 : 없음
# def clean_app():
#     이 기능은 모듈을 사용 해야함...
# =======================================================================
# 기능 구현
# =======================================================================
print(f'[[프로그램 시작]]')
while True:
    display_menu()
    # 사용자로 부터 메뉴 선택 받기
    select = input(f'메뉴 선택 : ')
    if select == '4': break
    elif select == '1':
        display_file_name()
    elif select == '2':
        search = input(f'이름 혹은 전화번호 : ')
        search_addr(search)
    elif select == '3':
        add = input(f'이름, 전화번호, 지역(예/홍길동,xxxxxxxxxxx,서울 : ').split(',')
        # name, phone, location = input(f'이름, 전화번호, 지역(예/홍길동,xxxxxxxxxxx,서울 : ').split(',')
        # 으로 해도됨.
        add_addr(add[0], add[1], add[2])
    else:
        print(f'메뉴 선택 오류.')
print(f'[[프로그램 종료]]')