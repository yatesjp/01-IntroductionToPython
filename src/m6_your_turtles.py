"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jonah Yates.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

myTurtle = rg.SimpleTurtle()
myTurtle.pen = rg.Pen('Red',9)
myTurtle.speed = 4

myTurtle.pen_up()
myTurtle.forward(50)
myTurtle.pen_down()

stopSize = 45
for n in range(6):
    for k in range(8):
        myTurtle.forward(stopSize)
        myTurtle.right(45)
    myTurtle.right(60)

theirTurtle = rg.SimpleTurtle()
theirTurtle.pen = rg.Pen('Midnight Blue',2)
theirTurtle.speed = 10

theirTurtle.pen_up()
theirTurtle.right(135)
theirTurtle.forward(300)
theirTurtle.pen_down()
theirTurtle.right(45)

for q in range(60):
    theirTurtle.forward(q*3)
    theirTurtle.right(180-q)




window.close_on_mouse_click()