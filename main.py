import pyautogui
from pynput import keyboard

width, height = pyautogui.size()

def on_press(key):
    # VIBECODED ========================
    vk = getattr(key, 'vk', None)   # virtual-key code (Windows)
    if vk == 111:                   # 111 = / symbol in windows
        pyautogui.moveTo(width/2, 60)
        pyautogui.leftClick()
    # VIBECODED =========================

    if key == keyboard.Key.alt_gr:
            # Stop listener
            return False    
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))      


# def on_release(key):
#     print('{0} released'.format(
#         key))


# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener: #on_release=on_release
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()
