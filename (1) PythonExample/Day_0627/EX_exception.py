# ============================================================================================
# EXCEPTION HANDLING 예외 처리.
# 프로그램 실행 시 발생하는 오류(error)에 대한 처리를 해준다.
# 오류가 발생 해도 프로그램이 중단되지 않고 실행될 수 있도록 예외처리해준다.
# ============================================================================================
num_1, num_2 = 10, 0
try:
    print(f'{num_1} / {num_2} = {num_1 / num_2}')
except Exception as errorname:
    print(f'ERROR OCCURRED / ERROR NAME = ', errorname)
finally:
    # 오류 발생 여부 상관없이 무조건 실행됨
    print(f'무조건 실행되는 구문')
print(f'END')

try:
    file = open(r'aaa.jpg')
    print(file.read())
    file.close()
except Exception as errorname:
    print(f'ERROR OCCURRED / ERROR NAME = ', errorname)
