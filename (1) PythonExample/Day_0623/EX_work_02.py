# =======================================================================
# comment.html 파일을 복사해서 home.txt파일로 만들기.
# 함수명 : filecopy로 만들기.
# 매개변수 : 파일명
# 반환값 : 없음
# =======================================================================


def filecopy_to_txt(filename):
    filename_edit = filename.split('/')[-1].split('.')[0] + '.txt'
    print(f'{filename_edit}')
    filepath = filename.split('/')
    del filepath[-1]
    filepath = '/'.join(filepath) + '/'
    open(filepath + filename_edit, 'w')
    


filecopy_to_txt(r'./comment save/comment.html')