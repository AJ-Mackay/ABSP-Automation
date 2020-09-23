# Module 16 - GUI Automation: Screenshots and Image Recognition

### ONCE AGAIN, the Shell has stopped responding to commands... ###
### "pyautogui.locateCenterOnScreen('file path/image name.file type') == None" returns "True" ###

import pyautogui

pyautogui.screenshot('/Users/paulmackay/Desktop/Python/GUI Automation/screenshotExample.png')
# Returns a Pillow object, arg is file path & image name.

pyautogui.locateOnScreen('/Users/paulmackay/Desktop/Python/GUI Automation/calc7key')
# Returns a tuple in the following format - (X axis co-ordinate, Y axis co-ordinate, width, height).

pyautogui.locateCenterOnScreen('Users/paulmackay/Desktop/Python/GUI Automation/calc7key.png')
# Returns the X axis & Y axis co-ordinates.

pyautogui.moveTo((x-axis, y-axis), duration=1) # Moves the mouse the the given co-ordinates over 1 second.
pyautogui.click(x-axis, y-axis) # Can be passed as two arguments, or as a tuple. e.g pyautogui.click((932, 336))

### Further Reading: ###
# https://automatetheboringstuff.com/chapter17
# https://pyautogui.readthedocs.org
