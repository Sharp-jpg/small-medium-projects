import turtle

def tic_tac_toe():

    window = turtle.getscreen()
    window = window.bgcolor("black")
    vert_line_left = turtle.Turtle()
    turtle.hideturtle()
    vert_line_left.pensize(15)
    vert_line_left.pencolor("white")
    vert_line_left.hideturtle()
    vert_line_left.penup()
    vert_line_left.setpos(-125, -200)
    vert_line_left.left(90)
    vert_line_left.pendown()
    vert_line_left.forward(500)

    vert_line_right = turtle.Turtle()
    turtle.hideturtle()
    vert_line_right.pensize(15)
    vert_line_right.pencolor("white")
    vert_line_right.hideturtle()
    vert_line_right.penup()
    vert_line_right.setpos(125, -200)
    vert_line_right.left(90)
    vert_line_right.pendown()
    vert_line_right.forward(500)

    horiz_line_top = turtle.Turtle()
    turtle.hideturtle()
    horiz_line_top.pensize(15)
    horiz_line_top.pencolor("white")
    horiz_line_top.hideturtle()
    horiz_line_top.penup()
    horiz_line_top.setpos(-300, 125)
    horiz_line_top.pendown()
    horiz_line_top.forward(575)

    horiz_line_bottom = turtle.Turtle()
    turtle.hideturtle()
    horiz_line_bottom.pensize(15)
    horiz_line_bottom.pencolor("white")
    horiz_line_bottom.hideturtle()
    horiz_line_bottom.penup()
    horiz_line_bottom.setpos(-300, -40)
    horiz_line_bottom.pendown()
    horiz_line_bottom.forward(575)


#winning lines

    def win_line_vert_left():

        winlinevertleft = turtle.Turtle()
        turtle.hideturtle()
        winlinevertleft.pensize(15)
        winlinevertleft.pencolor("white")
        winlinevertleft.hideturtle()
        winlinevertleft.penup()
        winlinevertleft.setpos(-200, -200)
        winlinevertleft.left(90)
        winlinevertleft.pendown()
        winlinevertleft.forward(500)


    def win_line_vert_middle():

        winlinevertmiddle = turtle.Turtle()
        turtle.hideturtle()
        winlinevertmiddle.pensize(15)
        winlinevertmiddle.pencolor("white")
        winlinevertmiddle.hideturtle()
        winlinevertmiddle.penup()
        winlinevertmiddle.setpos(0, -200)
        winlinevertmiddle.left(90)
        winlinevertmiddle.pendown()
        winlinevertmiddle.forward(500)


    def win_line_vert_right():

        winlinevertright = turtle.Turtle()
        turtle.hideturtle()
        winlinevertright.pensize(15)
        winlinevertright.pencolor("white")
        winlinevertright.hideturtle()
        winlinevertright.penup()
        winlinevertright.setpos(200, -200)
        winlinevertright.left(90)
        winlinevertright.pendown()
        winlinevertright.forward(500)


    def win_line_horiz_top():

        winlinehoriztop = turtle.Turtle()
        turtle.hideturtle()
        winlinehoriztop.pensize(15)
        winlinehoriztop.hideturtle()
        winlinehoriztop.pensize(15)
        winlinehoriztop.pencolor("white")
        winlinehoriztop.hideturtle()
        winlinehoriztop.penup()
        winlinehoriztop.setpos(-300, 200)
        winlinehoriztop.pendown()
        winlinehoriztop.forward(575)


    def win_line_horiz_middle():

        winlinehorizmiddle = turtle.Turtle()
        turtle.hideturtle()
        winlinehorizmiddle.pensize(15)
        winlinehorizmiddle.hideturtle()
        winlinehorizmiddle.pensize(15)
        winlinehorizmiddle.pencolor("white")
        winlinehorizmiddle.hideturtle()
        winlinehorizmiddle.penup()
        winlinehorizmiddle.setpos(-300, 50)
        winlinehorizmiddle.pendown()
        winlinehorizmiddle.forward(575)


    def win_line_horiz_bottom():

        winlinehorizbottom = turtle.Turtle()
        turtle.hideturtle()
        winlinehorizbottom.pensize(15)
        winlinehorizbottom.hideturtle()
        winlinehorizbottom.pensize(15)
        winlinehorizbottom.pencolor("white")
        winlinehorizbottom.hideturtle()
        winlinehorizbottom.penup()
        winlinehorizbottom.setpos(-300, -125)
        winlinehorizbottom.pendown()
        winlinehorizbottom.forward(575)

    #quadrant functions

    def top_left():
        top_left_turtle = turtle.Turtle()
        top_left_turtle.hideturtle()
        top_left_turtle.penup()
        top_left_turtle.pensize(0)
        top_left_turtle.setpos(-225, 200)

        if counter % 2 != 0:
            crosses(-255, 175)
        else:
            noughts(-225, 175)


    def top_right():
        top_right_turtle = turtle.Turtle()
        top_right_turtle.hideturtle()
        top_right_turtle.penup()
        top_right_turtle.pensize(0)
        top_right_turtle.setpos(225, 200)

        if counter % 2 != 0:
            crosses(185, 175)
        else:
            noughts(225, 175)


    def bottom_right():
        bottom_right_turtle = turtle.Turtle()
        bottom_right_turtle.hideturtle()
        bottom_right_turtle.penup()
        bottom_right_turtle.pensize(0)
        bottom_right_turtle.setpos(225, -200)

        if counter % 2 != 0:
            crosses(185, -175)
        else:
            noughts(225, -175)


    def bottom_left():
        bottom_left_turtle = turtle.Turtle()
        bottom_left_turtle.hideturtle()
        bottom_left_turtle.penup()
        bottom_left_turtle.pensize(0)
        bottom_left_turtle.setpos(-225, -200)

        if counter % 2 != 0:
            crosses(-255, -175)
        else:
            noughts(-225, -175)


    def middle():

        middle_turtle = turtle.Turtle()
        middle_turtle.hideturtle()
        middle_turtle.penup()
        middle_turtle.pensize(0)
        middle_turtle.setpos(0, 0)

        if counter % 2 != 0:
            crosses(-30, 0)
        else:
            noughts(0, 0)


    def bottom_middle():

        bottom_middle_turtle = turtle.Turtle()
        bottom_middle_turtle.hideturtle()
        bottom_middle_turtle.penup()
        bottom_middle_turtle.pensize(0)
        bottom_middle_turtle.setpos(0, -225)

        if counter % 2 != 0:
            crosses(-30, -175)
        else:
            noughts(0, -175)


    def top_middle():

        top_middle_turtle = turtle.Turtle()
        top_middle_turtle.hideturtle()
        top_middle_turtle.penup()
        top_middle_turtle.pensize(0)
        top_middle_turtle.setpos(0, 225)

        if counter % 2 != 0:
            crosses(-30, 175)
        else:
            noughts(0, 175)


    def left_middle():

        left_middle_turtle = turtle.Turtle()
        left_middle_turtle.hideturtle()
        left_middle_turtle.penup()
        left_middle_turtle.pensize(0)
        left_middle_turtle.setpos(-225, 0)

        if counter % 2 != 0:
            crosses(-255, 0)
        else:
            noughts(-225, 0)


    def right_middle():

        right_middle_turtle = turtle.Turtle()
        right_middle_turtle.hideturtle()
        right_middle_turtle.penup()
        right_middle_turtle.pensize(0)
        right_middle_turtle.setpos(225, 0)

        if counter % 2 != 0:
            crosses(175, 0)
        else:
            noughts(225, 0)


    #begin game

    print("\nplayer 1 is x's")
    print("player 2 is o's\n")

    counter = 0
    while counter != 9:
        counter += 1
        if counter % 2 !=0:
            turn = input("player1's turn, enter quadrant: ")
        elif counter % 2 == 0:
            turn = input("player2's turn, enter quadrant: ")

        if turn == "tl":
            top_left()
        elif turn == "tm":
            top_middle()
        elif turn == "tr":
            top_right()
        elif turn == "lm":
            left_middle()
        elif turn == "m":
            middle()
        elif turn == "rm":
            right_middle()
        elif turn == "bl":
            bottom_left()
        elif turn == "bm":
            bottom_middle()
        elif turn == "br":
            bottom_right()
        elif turn == "end":
            break


        #win logic WIP

        # horizontal top, middle, bottom for crosses
     #   if (crosses(-225, 200) and crosses(0, 225) and crosses(225, 200)):
     #       win_line_horiz_top()
     #   if crosses(-225, 0) and crosses(0,0) and crosses(225, 0):
     #       win_line_horiz_middle()
     #   if crosses(-225, -200) and crosses(0, -225) and crosses(225, -200):
     #       win_line_horiz_bottom()

        #vertical left, middle, right for crosses
        #if crosses(-225, 200) and crosses()





def noughts(x, y):          #defines o's

    circle = turtle.Turtle()
    circle.hideturtle()
    circle.pensize(10)
    circle.penup()
    circle.setpos(x, y)
    circle.pendown()
    circle.color("cyan")
    circle.circle(50)


def crosses(x, y):         #defines x's
    turtle.hideturtle()
    crosses = turtle.Turtle()
    crosses.hideturtle()
    crosses.color("black")
    crosses.setpos(x, y)
    crosses.pensize(10)
    crosses.color("red")
    crosses.left(45)
    crosses.forward(100)   #starts drawing to the top right
    crosses.penup()
    crosses.left(-135)
    crosses.forward(75)
    crosses.pendown()
    crosses.left(225)
    crosses.forward(105)   #starts drawing to the top left


tic_tac_toe()