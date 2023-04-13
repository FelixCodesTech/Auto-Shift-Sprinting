import keyboard as key
import time as t

while True:
    t.sleep(1)
    if key.is_pressed("w"):
        print("pressed")
        key.press("shift")
    else:
        print("released")
        key.release("shift")