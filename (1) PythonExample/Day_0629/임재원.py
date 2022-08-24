# 필수조건 : 계산기 class 생성
class Clac:
    # 인스턴스 생성자
    def __init__(self, maker, color):
        self.maker = maker
        self.color = color
    # get, set 메소드(선택)
    def getData(self): return self.data
    def setData(self, data): self.data = data
    # 사용자 기능
    def plus(self, *data):
        data_sum = data[0]
        for i in range(1, len(data)):
            data_sum += data[i]
        print(data_sum)
    def minus(self, *data):
        data_minus = data[0]
        for i in range(1, len(data)):
            data_minus -= data[i]
        print(data_minus)
    def multi(self, *data):
        data_multi = data[0]
        for i in range(1, len(data)):
            data_multi *= data[i]
        print(data_multi)
    def div(self, *data):
        data_div = data[0]
        for i in range(1, len(data)):
            data_div /= data[i]
        print(data_div)
    # 사용자 인터페이스 UI
    def showUi(self):
        print(f'==== 계산기 ====')
        print(f'1. 덧셈')
        print(f'2. 뺄셈')
        print(f'3. 곱셈')
        print(f'4. 나눗셈')
        print(f'5. 종료')
        print(f'===============')


myCalc = Clac('sharp', 'pink')
while True:
    myCalc.showUi()
    select = input('선택 : ')
    if select == '5':
        break
    elif select == '1':
        myCalc.plus(3, 3, 3)
    elif select == '2':
        myCalc.minus(10, 2, 1, 1)
    elif select == '3':
        myCalc.multi(3, 2, 2)
    elif select == '4':
        myCalc.div(642, 2, 5, 12)

