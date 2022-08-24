# 벽돌 깨기 게임 만들기
nickname = ''
level = 0
score = 0
ranking = 0
# 게임하는 사람의 정보 입력 받기
# 함수명 : set_player
# 파라미터 : 없음(input으로 받자.)
# 반환값 : 없음
def set_player():
    nickname = input(f'닉네임 : ')
    level = 0
    score = 0
    ranking = 0
# 메뉴 출력하기
# 함수명 : display_menu
# 파라미터 : 없음
# 반환값 : 없음
def display_menu():
    print(f'1. 회원가입')
    print(f'2. 게임시작')
    print(f'3. 랭킹보기')
    print(f'4. 종   료')
# 프로그램 코드
while True:
    display_menu()
    select = input(f'메뉴선택 : ')
    if select == '4':break
    elif select == '1':
        set_player()
class player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.level = 0
        self.score = 0
        self.ranking = 0
    # 이 class의 인스턴스 변수들의 값을 업데이트 또는 읽기 하는 메소드를 넣는다
    # set method, get method
    def set_level(self, level):
        self.level = level
    def set_scorel(self, score):
        self.score = score
    def set_ranking(self, ranking):
        self.ranking = ranking
    def get_nickname(self):
        return self.nickname
    def get_level(self):
        return self.level