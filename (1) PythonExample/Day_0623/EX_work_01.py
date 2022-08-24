# =======================================================================
# 사용자가 작성한 코멘트를 파일로 저장하기.
# 조건 : 키보드로 코멘트를 입력 받을 것.
#       입력 받은 코멘트는 누적 될 것.
#       댓글을 입력하는 기능을 무한 반복으로 입력 받되, 종료 조건으로 q or Q 입력
# =======================================================================
message = []
while True:
    message_input = input(f'코멘트를 입력해 주세요. : ')
    message.append(message_input)
    if message_input == 'q' or message_input == 'Q':
        del message[-1]
        break
print(f'{"=" * 50}')
print(f'작성된 코멘트는 {message}입니다.')
print(f'comment.html 파일에 저장 합니다.')
print(f'{"=" * 50}')
file = r'./comment save/comment.html'
with open(file, mode='a', encoding="UTF-8") as file:
    for i in range(len(message)):
        file.write(message[i] + '\n')
# =======================================================================
# 강사님 코드
# =======================================================================
file = r'./comment save/comment.html'
with open(file, mode='a', encoding="UTF-8") as file:
    while True:
        text = input(f'코멘트를 입력해 주세요 : ')
        if text in ['q', 'Q']:
            break
        file.write(text + '\n')
