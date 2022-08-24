# ============================================================================================
# 사용자 정의 class
# ex) 학생을 표현하는 데이터 타입을 만들고 싶음.
# 학생이 가지고 있는 특징, 성질, 외형 -> 변수(field, attribute)(교복, 학교, 학년, 담임, 반, 성적 등 ...)
#                 역할, 기능 -> 메서드(method)(공부한다, 학교에 간다, 시험친다 등 ...)
# ============================================================================================
class student:
    def __init__(self, uniform, school, grade, shcool_class):     # initialize(초기화)
        self.uniform = uniform
        self.school = school
        self.grade = grade
        self.shcool_class = shcool_class

    def go_shcool(self, uniform, school):
        print(uniform + school)

    def study(self, uniform, school, grade):
        print(uniform + school + grade)


me = student(0, 0, 0, 0)
me.go_shcool('교복', '학교')
# ============================================================================================
# 클래스명 -> student2
# 속성 -> 학번(std_num), 학교(school), 학년(grade)
# 기능 -> 공부한다, 시험친다
# ============================================================================================


class student2:
    # 클래스 변수 -> 모든 인스턴스가 공유하는 값
    school = '경북대'

    # 객체 생성 시 초기화 메서드
    def __init__(self, std_num, year, grade):
        self.std_num = std_num
        self.year = year
        self.grade = grade

    # student class의 역할 기능
    # 000이 00과목을 공부한다.
    def study(self, subject):
        print(f'{self.std_num}는 {subject}을/를 공부한다.')

    # 000이 00시험을 친다
    def test(self, title):
        print(f'{self.std_num}는 {title}을/를 시험친다.')

    # 학생 정보 출력 기능 -> 학번, 학년, 학교를 출력
    def std_info(self):
        print(f'학교 = {self.school}')
        print(f'학년 = {self.year}')
        print(f'학번 = {self.std_num}')


# 객체 즉, student 인스턴스를 생성 하고 싶다.
std_1 = student2('001', 3, 4.3)
std_2 = student2('002', 2, 3.7)
std_1.std_info()
