import cv2
import keyboard
import numpy as np
from pynput.mouse import Button, Controller
from pywinauto import Application
from pywinauto.findwindows import find_window

mouse = Controller()

switch_b = False
def switch():
    global switch_b
    switch_b = not switch_b
keyboard.add_hotkey("F9", switch)

def click_star(frame, template):
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    if max_val > 0.8:  
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(frame, f"{max_val:.2f}", (top_left[0], top_left[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        rect = window.rectangle()
        window_x, window_y = rect.left, rect.top

        x = window_x + top_left[0] + (w // 2)
        y = window_y + top_left[1] + (h // 2)

        if switch_b:
            mouse.position = (x, y)
            mouse.click(Button.left)
        

window_title = "TelegramDesktop"
app_path = r"C:\Users\Work\AppData\Roaming\Telegram Desktop\Telegram.exe"
app = Application().start(app_path) 
window_handle = find_window(title=window_title)
window = app.window(handle=window_handle)

templates = [cv2.imread('images/20.png'), cv2.imread('images/25.png'), cv2.imread('images/30.png'), cv2.imread('images/35.png'), cv2.imread('images/40.png'), cv2.imread('images/play.png')]

while True:
    if switch_b:
        print("On")
    else:
        print("Off")

    window_capture = window.capture_as_image()
    frame = np.array(window_capture)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    for template in templates:
        click_star(frame, template)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()