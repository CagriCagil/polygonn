import turtle
''' polygon '''
''' ekran ile ilgili kodlar '''
drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("py_turtle")

''' turtle ile ilgili kodlar '''
side_num = int(input("Enter side number: "))
side_length = int(input("Enter side length: "))
angle = 360.0 / side_num

turtle_instance = turtle.Turtle()
for i in range(side_num):
    turtle_instance.forward(side_length)
    turtle_instance.right(angle)

turtle.done()