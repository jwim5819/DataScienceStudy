# ==============================================================================================
# 파이썬에서 미리 만들어서 제공하는 class가 있다. 예) int, float, list, dic, str, tuple 등
num = 123
num2 = int(123)     # 두 코드는 같은걸 의미한다.
name = 'hong'
name2 = str('hong')     # 실제로는 str()생성자가 실행이 되었다.
# ==============================================================================================
# 클래스를 만드는 기준 = 누가봐도 같은 기능을 하는 것들을 묶을때 class를 사용하자
# 내가 만드는 class -> 평면에 좌표값을 저장하는 data
# class명 : point
# 변수(속성, 특징) : x, y
# 함수(메소드, 역할, 기능)
#  - point class로 메모리에 존재하는 객체 생성하는 메소드 -> __init__(self, x, y)
#  - 객체(인스턴스)의 값을 읽어주는 메소드 -> get속성(변수)명() -> 현재 속성값을 반환해줌
#  - 객체의 값을 변경시켜주는 메소드 -> set속성(변수)명()
# 위의 3개는 거의 필수 메소드이다.
#  - 추가로 내가 원하는 기등의 메소드를 만들어주면 됨
class point:
    # point instance를 생성하는 메소드
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # point 인스턴스에 저장된 변수값을 읽어오는 메소드
    def getx(self): return self.x
    def gety(self): return self.y
    def getinstance(self): return self.x, self.y
    # point 인스턴스에 저장된 변수값을 변경하는 메소드
    def setx(self, x): self.x = x
    def sety(self, y): self.y = y
    def setinstance(self, x, y):
        self.x = x
        self.y = y
    # 내가 원하는 기능의 메소드
    # 현재 point 객체의 정보를 출력하는 메소드
    def show_point_info(self):
        print(f'현재 좌표 값 (x = {self.x}, y = {self.y})')
    # point 인스턴스에 해당하는 좌표를 그리는 메소드
    # x값은 가로로 이동, y값은 세로로 이동
    def print_point(self):
        print('\n' * self.y, end='')
        print('  *' * (self.x - 1), end='')
        print(f'  ★{self.x,self.y}')
# point 인스턴스 생성하기
p1 = point(10, 5)
p1.setx(15)
print(p1.getinstance())
p1.x = 25
print(p1.getinstance())     # 근데 왜 굳이 set 메소드를 써서 표현하나? -> 정통적인 객체지향 언어에서는 set메소드로만 값을 바꿀 수 있기 때문. 파이썬이 관대하다.
p1.z = 123
print(p1.z, end='')     # 심지어 없는 변수를 집어넣어도 print 했을 시 나옴 -> 너무 관대하다.
p1.print_point()
