# 클래스명 : 스파게티
# 재료 : 채소, 면, 소스, 기타재료
# 기능 : 재료손질, 면삶기, 조리, 먹기
# ================================================
# 스파게티 class 생성
class spaghetti:
    water = 'boiled water'      # 클래스변수 생성
    spaghetti_name = ''

    def __init__(self, sauce, noodle, ingredient):      # 인스턴스 생성자
        self.sauce = sauce
        self.noodle = noodle
        self.ingredient = ingredient

    def make_spaghetti(self):       # 사용자 지정 메소드
        process = self.water + '+' + self.noodle + '삶기' + self.ingredient + '손질+' + self.sauce + '준비'
        self.spaghetti_name = self.ingredient + ' ' + self.sauce + ' ' + self.noodle
        print(f'준비과정 : {process}')
        print(f'[{self.spaghetti_name}]이/가 만들어 졌습니다.')

    def eat_spaghetti(self):
        print(f'{self.spaghetti_name}을 먹습니다.')

spaghetti_1 = spaghetti('oil', 'spaghetti', 'garlic')
spaghetti_1.make_spaghetti()
spaghetti_1.eat_spaghetti()



