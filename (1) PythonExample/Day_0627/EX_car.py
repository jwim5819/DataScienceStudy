# ============================================================================================
# 현대 자동차를 표현하는 class를 만들어라
# class명 -> car
# 속성 -> 제조사, 차번호, 차종류, 차색상
# 기능 -> 이동한다, 정지한다, 차 정보 출력
# class변수 -> 제조사
# instance 변수 -> 차번호, 차종류, 차색상
# 이동한다 -> 0000번 자동차가 00에서 00으로 이동한다.
# 정지한다 -> 0000번 자동차가 000에 정지했다.
# 차 정보 출력 -> 제조사, 차번호, 차종류, 차색상 등등 출력
# ============================================================================================

class car:
    brand = '현대자동차'

    def __init__(self, car_num, car_type, car_color):
        self.car_num = car_num
        self.car_type = car_type
        self.car_color = car_color

    def car_move(self, start, stop):
        print(f'{self.car_num}번 자동차가 {start}에서 {stop}으로 이동한다.')

    def car_stop(self, where):
        print(f'{self.car_num}번 자동차가 {where}에 정지했다.')

    def car_info(self):
        print(f'==========차량 정보==========')
        print(f'제조사 = {car.brand}')
        print(f'차번호 = {self.car_num}')
        print(f'차종류 = {self.car_type}')
        print(f'차색상 = {self.car_color}')
        print(f'============================')


mycar = car('8372', '승용차', '검정색')
mycar.car_move('거제', '대구')
mycar.car_stop('동대구역')
mycar.car_info()

my2ndcar = car('2412', '승용차', '파란색')
my2ndcar.car_move('대구', '서울')
my2ndcar.car_stop('서울역')
my2ndcar.car_info()

# car 데이터 10개 저장하기.
cars = []
for i in range(1, 10):
    cars.append(car(i*1111, '승용차', '핑크'))

for car in cars:
    print(f'{car.car_num}')

