# 라이브러리란 도구를 말함
# 누군가 미리 만들어놓은 프로그램(도구)을 활용하여 사용
# 설치방법 pip install pyautogui
# 공식문서 https://pyautogui.readthedocs.io/en/latest/index.html
# 독학하는 방법 => 공식문서 활용
# 튜플 데이터가 변하지 않는 리스트 ()


# sys모듈은 파이썬 인터프리터를 제어 할 수 있고
# os 모듈은 운영체제를 제어 할 수 있다

import sys
import pyautogui
# 마우스 커서 위치 좌표
# print(pyautogui.position())

# 화면 해상도 크기
# print(pyautogui.size())

'''
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        # rjust는 정렬함수이다
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')'''

# 마우스 움직임
#pyautogui.moveTo(100, 200)

# 5초에 걸쳐서 마우스 움직임
#pyautogui.moveTo(100, 200, 5)

# 픽셀 단위로 마우스 커서 이동
#pyautogui.move(100, 200)

# 마우스 드래그 left right middle
#pyautogui.dragTo(100, 200, button='left')

# 마우스 클릭
#pyautogui.click()

# 특정 위치 클릭
#pyautogui.click(x=100, y=200)

# 클릭할 때 다른 마우스 버튼 지정 가능
#pyautogui.click(button='right')

# 더블클릭
#pyautogui.click(clicks=2, interval=0.25)

# enter 키를 3초에 한번씩 세번 입력합니다.
pyautogui.press('enter', presses=3, interval=3)

'''
>>> pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click
>>> pyautogui.mouseDown(button='right')  # press the right button down
>>> pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.'''