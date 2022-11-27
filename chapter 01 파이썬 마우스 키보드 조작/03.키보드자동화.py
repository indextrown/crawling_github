import pyautogui
import pyperclip  # 카피 명령어 한글 복사할 때 사용
# 키보드 입력(문자)
#pyautogui.write('startcoding', interval=0.25)

# 키보드 입력(키)
#pyautogui.press('enter')
#pyautogui.press('up')

# 키보드 입력(여러개 동시에)
#pyautogui.hotkey('ctrl', 'c')

# 한글 입력 방법
pyperclip.copy('스타트코딩')
pyautogui.hotkey('ctrl', 'v')
