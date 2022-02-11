from turtle import *

speed(0)

begin_fill()
color("red", "red")
goto(0,-1000)
circle(1000)
end_fill()

penup()

goto(-120,200)

pendown()

begin_fill()
color("white", "white")

right(135)
forward(35)

pendown()

circle(200)

end_fill()

goto(0,0)

begin_fill()
color("black", "black")

for i in range(4):
    forward(100)
    right(90)

    forward(150)
    right(90)

    forward(50)
    right(90)

    forward(100)
    left(90)

    forward(50)
    left(90)

end_fill()

done()
