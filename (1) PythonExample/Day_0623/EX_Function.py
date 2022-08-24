# =======================================================================
# 함수(Function)는 왜 사용하나? 동일 혹은 유사한 코드를 계속 쓰는걸 방지하기 위해서
# 컴퓨터 메모리의 효율적인 사용을 위해서.
# 특별한 기능을 가지는 코드를 정의 해놓고 '재사용' 하고싶어서.
# def 함수명(매개변수1, 매개변수2, ....):
#     코드
#     코드
#     return 결과
# =======================================================================
# 기능 : 숫자 2개 더한 후 결과 돌려주는 기능
# 이 기능을 내포하는 함수명 정하기 : add_2
# 기능에 필요한 매개변수 : a, b
# 반환값 : add_result
# =======================================================================
def add_2(a, b):
    """
    숫자 2개를 더한 후 결과를 반환하는 함수
    :param a: 정수(int)
    :param b: 정수(int)
    :return: result
    """
    result = a + b
    return result


result_2 = add_2(39, 24)
print(f'{result_2}')
# =======================================================================
# 기능 : 문자 2개를 더하는 기능의 함수
# 함수명 : str_add
# 매개변수 : a, b
# 반환여부 : result 반환
# =======================================================================
def str_add(a, b):
    return str(a) + str(b)


result = str_add('ABC', 'DEF')
print(f'{result}')
# =======================================================================
# 기능 : 원하는 단의 구구단을 출력하는 함수
# 함수명 : gugudan
# 매개변수 : a
# 반환여부 : print로 출력만 하고 결과값 반환하지 않음.
# =======================================================================
def gugudan(a):
    print(f'{a}단 출력 결과.')
    for i in range(1, 10):
        print(f'{a} * {i} = {a * i}')


gugudan(8)
# =======================================================================
# 가변인수를 가지는 함수.
# 유사하거나 동일한 코드일때 코드는 그대로 두되 매개변수의 갯수만 변할 수 있도록.
# *매개변수명 -> 0 ~ n개의 인자가 들어올 수 있다는 약속. (파이썬 에서만)
# 즉 변수가 없어도 되고 많아도 된다.
# =======================================================================
def add_num(*nums):
    print(f'{type(nums)}')
    total = 0
    for num in nums: total += num
    return total


print(add_num(10))
print(add_num(1, 4, 5, 2, 34, 2, 4, 3, 19))
# =======================================================================
# 기능 : 평균 구하는 함수
# 함수명 : get_avg
# 파라미터 : 과목, 점수 유동적임 **subject
# 반환값 : 평균 -> float 형태일것임
# =======================================================================
def get_avg(**subject):
    print(f'{type(subject)}')
    values = subject.values()
    total = 0
    for value in values:
        total += value
    return total / len(values)


print(f'{get_avg(국어=98, 영어=80):.2f}')