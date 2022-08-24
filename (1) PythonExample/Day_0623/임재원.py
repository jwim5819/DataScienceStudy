import os.path
import os


def dir_check():        # 프로그램 시작 시 address_book 폴더의 존재 유무를 확인하여 폴더 추가 결정
    dir_path = r'./address_book'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)  # 하나의 폴더만 생성할 때


def main_menu():       # 메인 메뉴 표시 함수
    print(f'==========나의 주소록==========')
    print(f'{"1. 전체보기 : 1번":^26}')
    print(f'{"2. 검   색 : 2번":^27}')
    print(f'{"3. 추   가 : 3번":^27}')
    print(f'{"4. 종   료 : 4번":^27}')
    print(f'=============================')


def menu_3():       # 주소록을 추가하는 함수
    while True:         # 양식에 맞게 입력하지 않았을 때는 잘못된 입력입니다를 출력 후 새로 입력을 받는다.
        try:
            address_info = input(f'이름, 전화번호, 지역을 입력해주세요(","로 구분) : ')
            address_info_split = address_info.split(',')
            filename = address_info_split[0]+'_'+address_info_split[1]+'.txt'
            file_dir = r'./address_book/' + filename
            if not os.path.isfile(file_dir):        # 만약 addressbook에 같은 이름을 가진 파일이 없다면 파일을 만들 것
                file = open(file_dir, mode='w', encoding="UTF-8")
                file.write(address_info)
                file.close()
            return True
        except IndexError:
            print(f'잘못된 입력입니다. 양식을 확인해 주세요.')


def menu_1():       # addressbook의 정보를 읽어와서 화면에 표시해주는 함수
    path = "./address_book"
    file_list = os.listdir(path)       # addressbook의 정보를 읽어 옵니다.
    print(f'==========파일 리스트==========')
    for i in range(len(file_list)):
        print(f'{file_list[i]}')
    print(f'=============================')


def menu_2():       # 이름이나 전화번호를 입력하면 검색 후 화면에 표시해주는 함수.
    name = input(f'검색 단어(이름 혹은 전화번호) : ')       # 이름 혹은 전화번호가 완전히 같지 않더라도 검색이 되고 이름이나 전화번호가 겹치는 파일도 모두 표시해 준다.
    path = "./address_book"
    file_list = os.listdir(path)
    for i in range(len(file_list)):
        if name in file_list[i]:
            print(f'파일명 : {file_list[i]}')
            file_open = r'./address_book/' + file_list[i]
            file = open(file_open, mode='r', encoding='UTF-8')
            line = file.read()
            print(f'내 용 : {line}')


def address_book_main():      # 종료를 입력하기 전 까지 메뉴 표시와 메뉴 입력받기 무한 반복
    dir_check()     # address_book 폴더 유무 확인
    while True:
        main_menu()
        number = input(f'원하시는 메뉴를 숫자로 선택해 주세요. : ')
        if number == '1':
            menu_1()
        elif number == '2':
            menu_2()
        elif number == '3':
            menu_3()
        elif number == '4':
            print(f'프로그램을 종료합니다.')
            break
        else:
            print(f'없는 메뉴입니다. 다시 선택해주세요.')


address_book_main()
