"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jonah Yates.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   Write code that constructs a SimpleTurtle with a red Pen
#   and makes it move around a bit.  Don't forget to:
#     -- import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     -- ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

myTurtle = rg.SimpleTurtle()
myTurtle.pen = rg.Pen('Red',9)
myTurtle.speed = 4

for k in range(8):
    myTurtle.forward(45)
    myTurtle.right(45)

window.close_on_mouse_click()