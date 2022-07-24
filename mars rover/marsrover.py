import re
import turtle
import os

os.chdir("D:\\Phyton\\101computing\\mars rover")
def mission_1():
    rover.forward(335)
    rover.left(90)
    rover.forward(335)
    rover.left(90)
    rover.forward(335)
    rover.left(90)
    rover.forward(335)
def mission_2():
    
    for i in range(4):
        rover.forward(335)
        rover.left(90)
def mission_3():
    for i in range(5):
        rover.forward(335)
        rover.left(90)
        rover.forward(50)
        rover.left(90)
        rover.forward(335)
        rover.right(90)
        rover.forward(50)
        rover.right(90)
    rover.forward(335)

def mission_4():
    forward=335
    up=33.5
    rover.forward(forward)
    rover.left(90)
    rover.forward(forward)
    rover.left(90)
    rover.forward(forward)
    rover.left(90)
    for i in range(1,10):
        rover.forward(forward-up*i)
        rover.left(90)
        rover.forward(forward-up*i)
        rover.left(90)
def mission_5():
    rover.left(17)
    rover.forward(230)
    rover.left(45)
    rover.forward(150)
    rover.left(107)
    rover.forward(205)
    rover.left(80)
    rover.forward(250)
def mission_6():
    rover.left(11)
    rover.forward(150)
    rover.right(40)
    rover.forward(200)
    rover.right(90)
    rover.forward(320)
    rover.right(90)
    rover.forward(150)
    rover.right(55)
    rover.forward(100)
def mission_7():
    for i in range(12):
        rover.forward(92)
        rover.left(30)
screen=turtle.Screen()
screen.setup(400,400)
screen.bgpic("mars-path-1.png")
rover=turtle.Turtle()
screen.addshape("rover.gif",shape=None)
rover.shape("rover.gif")
rover.shapesize(0.5,0.5,0.5)
rover.speed(1)

rover.color("#810000")
rover.pensize(2)
rover.penup()
# rover.goto(-165,-165) missions 1,2,3,4
# rover.goto(-160,-135) # mission 5
# rover.goto(-160,160) # mission 6
rover.goto(-40,-160)
rover.pendown()

# mission_1()
# mission_2()
# screen.bgpic("mars-path-2.png")
# mission_3()    
# screen.bgpic("mars-path-3.png")
# mission_4()    
# screen.bgpic    ("mars-path-4.png")
# mission_5()
# screen.bgpic("mars-path-6.png")
# mission_6()
screen.bgpic("mars-path-5.png")
mission_7()
turtle.exitonclick()