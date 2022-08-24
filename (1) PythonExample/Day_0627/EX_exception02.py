# ============================================================================================
# 프로그램 기능 구현 상 강제로 예외(오류) 발생시키기
# raise 예외객체
# ============================================================================================
try:
    num = int(input(f'3의 배수 입력 : '))
    if num % 3 != 0:
        print(f'{num}은 3의 배수가 아닙니다.')
        raise Exception('3의 배수 오류')
except Exception:
    print(f'ERROR 발생')


class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    pass


eagle = Eagle()
eagle.fly()
