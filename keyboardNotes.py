# Module 16 - GUI Automation: Controlling the Keyboard from Python

import pyautogui
pyautogui.click(904, 481); pyautogui.typewrite('Hello world!', interval=0.2)
# Commands can be separated by a semi-colon to run more than one on a single line.
# "interval=" is not required, you can just pass the time in as an argument.
# e.g - "pyautogui.click(904, 481); pyautogui.typewrite('Hello world!', 0.2)"
# works exactly the same. 

### Time to hit enter: ###

Hello world!

### I'm not going to lie. That was pretty awesome to watch! ###

pyautogui.KEYBOARD_KEYS # Returns a list of all available commands

# Keys can be passed individually as a list.
pyautogui.click(904, 481); pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], 1)
# The above line will print ab, press left arrow key twice then print XY with a 1 second delay between each key press.
# The resulting string will be "XYab".

pyautogui.press('f1') # Presses the F1 key, which opens the Python Documentation.
pyautogui.hotkey('command', 'o') # Results are the same as pressing cmd + o in combination, which is the "Open" function.
