import turtle

canvas = turtle.getscreen()
v_pen = turtle.Turtle()
v_pen.pensize(5)
v_pen.pencolor('green')
for _ in range(5):
    v_pen.forward(200)
    v_pen.right(72)     #360/4 = 90 (Rectangle) or #360/3 = 120 (Triangle) or #360/5 = 72 (Pentagone)

v_pen.hideturtle()
canvas.exitonclick()
