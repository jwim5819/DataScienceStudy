# ============================================================================================
# 상속(inheritance)
# 기존 class의 모든것을 가져와서(상속해서) 사용한다.
# 문법 -> class 클래스명(상속받아올 클래스명):
# ============================================================================================
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display_info(self):
        print(f'{self.x}, {self.y}')


class B(A):
    def calc(self):
        print(f'{self.x + self.y}')


b = B(15, 24)
b.display_info()
b.calc()


class C(B):
    def calc(self):        # 상속받은 기능을 바꾸는것 = 오버라이딩(overriding)
        print(f'수정도 가능합니다. {self.x + self.y}')

    def multi(self):
        print(f'{self.x * self.y}')


c = C(58, 126)
c.display_info()
c.calc()
c.multi()

