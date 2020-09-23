# Module 16 - GUI Automation: Controlling the Mouse from Python

### Co-ordinates Information ###
### X Axis is Left and Right. Negative numbers indicate to move left ###
### Y Axis is Up and Down. Negative numbers indicate to move UP ###

###################################################################
###                        * IMPORTANT *                        ###
###                                                             ###
###     THE Y AXIS WORKS OPPOSITE TO GRAPHS IN MATHEMATICS.     ###
###                                                             ###
###################################################################

import pyautogui

pyautogui.size() # Returns "Size(width=1440, height=900)" - Screen spec of this mac.
width, height = pyautogui.size() # Sets the variables to the appropriate size.
pyautogui.position() # Returns "Point(x=523, y=264)" which is the current position of the mouse cursor.

pyautogui.moveTo(10, 10) # Moves the cursor instantly to the given co-ordinates, in this case x=10, y=10.
pyautogui.moveTo(324, 270, duration=1.5) # Moves the cursor to the new co-ordinates over the given duration in seconds.
### The keyword "duration" is not required, you can just pass the time as a third argument. ###
### e.g pyautogui.moveTo(1313, 666, 7) ###

pyautogui.moveRel(200, -100, 2) # Moves the cursor 200 pixels to the right and up 100 pixels over 2 seconds from its current position.
### pyautogui.dragTo(arg1, arg2) - Will single click and hold as the cursor moves to the given co-ordinates. Add arg3 for duration. ###
### pyautogui.dragRel(arg1, arg2) - Will single click and hold as the cursor moves from its current position relative to the arguments given, arg3 is optional for duration. ###
### e.g pyautogui.dragRel(-100, 200, 3) - Moves the cursor left 100 pixels and down 200 pixels over 3 seconds. ### 
pyautogui.click(160, 507) # Instantly moves the cursor to the given co-ordinates and performs a single mouse click.
### To perform a single click in the cursor's current location, do not provide any arguments. ###

pyautogui.doubleClick(1372, 280) # Instantly moves the cursor to the co-ordinates provided and double clicks (which opens the C# folder on my desktop).
### .rightClick(arg1, arg2) is also an option. ###
### .middleClick(arg1, arg2) does not appear to work on Macs. ###
### Providing no arguments uses the cursor's current location.  ###

###################################################################
###                        * IMPORTANT *                        ###
###                                                             ###
###    If you ever lose control of the cursor while running     ###
###     pyautogui, slam the mouse into the top left corner      ###
###                                                             ###
###              THIS FAIL-SAFE STOPS THE PROGRAM.              ###
###                                                             ###
###################################################################

# If you run the following in terminal, you can quickly and easily find the desired co-ordinates of objects to write a script.
### Remember to start Python in the terminal first. ###
import pyautogui
pyautogui.displayMousePosition() # This will return the X co-ordinates, Y co-ordinates and the RGB details of the current pixel the cursor is on.
# e.g "X: 489 Y: 177 RGB:(0, 160, 0) - While the cursor is hovering over a green pixel.
# Press Ctrl + C to Quit.
### ONLY RUN THIS IN TERMINAL, NOT IDLE. ###

### Further reading at https://pyautogui.readthedocs.org ###
