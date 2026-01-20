
import pyautogui
import time

pyautogui.press('win')
time.sleep(1)  
pyautogui.write('microsoft edge ')  
time.sleep(1)
pyautogui.press('enter')   
time.sleep(5)
pyautogui.write("pokemon showdown")
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=400, y=800)  
time.sleep(5)    
pyautogui.press('tab', presses=6, interval=0.5)
pyautogui.press('enter')  
time.sleep(5)
