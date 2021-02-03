import pyautogui
import time

print('Write a text to send with emoticion (Only Alphabet)')
Text = input()
Text2 = list(Text)
Count = 0
print('Please Turn On Discord and Ready To Chatting in 10 seconds')
print(Text2)
time.sleep(10)
print('Lets Go')
print(pyautogui.position())

# :regional_indicator_
for i1 in Text2:
    pyautogui.press(':')
    pyautogui.press('r')
    pyautogui.press('e')
    pyautogui.press('g')
    pyautogui.press('i')
    pyautogui.press('o')
    pyautogui.press('n')
    pyautogui.press('a')
    pyautogui.press('l')
    pyautogui.press('_')
    pyautogui.press('i')
    pyautogui.press('n')
    pyautogui.press('d')
    pyautogui.press('i')
    pyautogui.press('c')
    pyautogui.press('a')
    pyautogui.press('t')
    pyautogui.press('o')
    pyautogui.press('r')
    pyautogui.press('_')
    pyautogui.press(Text2[Count])
    pyautogui.press(':')
    pyautogui.press('space')
    Count = Count + 1
    try:
        if Text2[Count] is None:
            break
    except:
        break
