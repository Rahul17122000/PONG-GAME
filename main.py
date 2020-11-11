from input_name import *
import turtle

#When ball touches the boundary or any bat then you will hear a sound. Here I uses my window sound.
import winsound

win=turtle.Screen()
win.setup(1200,700)
win.bgcolor('black')
win.title("AWESOME PONG GAME")


#Draw Border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color('blue')
border_pen.up()
border_pen.setposition(-500,-300)
border_pen.width(3)
border_pen.down()
border_pen.begin_fill()
border_pen.fillcolor('yellow')
border_pen.fd(1000)
border_pen.lt(90)
border_pen.fd(600)
border_pen.lt(90)
border_pen.fd(1000)
border_pen.lt(90)
border_pen.fd(600)
border_pen.end_fill()

border_pen.up()
border_pen.goto(0,0)
border_pen.down()
border_pen.hideturtle()

#actually the two controller are turtle

#Left Side Controller
left_bat=turtle.Turtle()
left_bat.speed(0)
left_bat.shape('square')
left_bat.color('black')
left_bat.shapesize(stretch_wid=6,stretch_len=2)
left_bat.up() 
left_bat.goto(-400, 0)

#Right Side Controller
right_bat=turtle.Turtle()
right_bat.speed(0)
right_bat.color('black')
right_bat.shape("square")
right_bat.shapesize(stretch_wid=6,stretch_len=2)
right_bat.up()
right_bat.goto(400,0)

#tennis ball
ball=turtle.Turtle()
ball.color('red')
ball.speed(0)#to increase the speed of the turtle
ball.up()#USE OF THIS LINE(To hide the line made by bal turtle when it is moving.)
ball.shape('circle')
ball.goto(0,0)#USE OF THIS LINE
ball.dx=5#THIS LINE
ball.dy=5#THIS LINE

#Score at starting of the match
First_Player=0
Second_Player=0

#Displaying Left/First Player Winnner Tag/Losing Tag
l_win=turtle.Turtle()
l_win.color("red")
l_win.speed(0)
l_win.width(4)
l_win.up()
l_win.hideturtle()

#Displaying Right/Second Player Winnner Tag/Losing Tag
r_win=turtle.Turtle()
r_win.color("red")
r_win.speed(0)
r_win.width(4)
r_win.up()
r_win.hideturtle()

#Displaying Left/First Player Score
l_score=turtle.Turtle()
l_score.color('red')
l_score.width(3)
l_score.speed(0)
l_score.up()
l_score.hideturtle()
l_score.goto(-500,300)
l_score.write("PLAYER "+firstplayer+" : 0",align='left',font=('Courier',28,'normal'))
#l_score.hideturtle()#this line must be written above bcz anyone can see what is happening on the game screen

#Displaying Right/Second Player score
r_score=turtle.Turtle()
r_score.color('red')
r_score.width(3)
r_score.speed(0)
r_score.up()
r_score.hideturtle()
r_score.goto(500,300)
r_score.write("PLAYER "+secondplayer+" : 0",align='right',font=('Courier',28,'normal'))


#Key definition to move bat vertically
speed=25
def batrup():
    y=right_bat.ycor()
    y+=speed
    if y>240:#setting boundary limit
        y=240
    right_bat.sety(y)
def batrdown():
    y=right_bat.ycor()
    y-=speed
    if y<-240:#setting boundary limit
        y=-240
    right_bat.sety(y)
def batlup():
    y=left_bat.ycor()
    y+=speed
    if y>240:#setting boundary limit
        y=240
    left_bat.sety(y)
def batldown():
    y=left_bat.ycor()
    y-=speed
    if y <-240:#setting boundary limit
        y=-240
    left_bat.sety(y)


#Key controller
win.listen()
win.onkeypress(batlup,'s')
win.onkeypress(batldown,'x')
win.onkeypress(batrup,'Up')
win.onkeypress(batrdown,'Down')

while True:
    win.update()

    #For movement of the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border
    if ball.ycor()>295:
        ball.sety(295)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.ycor()<-295:
        ball.sety(-295)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor()>495:
        ball.goto(0,0)
        #ball.setx(495b)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        First_Player+=1
        l_score.clear()
        l_score.write("PLAYER "+firstplayer+" : {}".format(First_Player),align='left',font=('Courier',28,'normal'))
        if First_Player==5:
            l_win.goto(0,200)
            l_win.write("WINNER :"+firstplayer,align='center',font=('Courier',36,'normal'))
            r_win.goto(0,-200)
            r_win.write("LOSER :"+secondplayer,align='center',font=('Courier',36,'normal'))
            #When screen will display the name of winner and loser so In order to hide the movement of ball we uses the below line
            ball.hideturtle()
            #To keep the graphics window open
            input()
            #l_win.goto(0,0)
            #r_score.goto(0,0)        
        
    if ball.xcor()<-495:
        ball.goto(0,0)
        #ball.setx(-495)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        Second_Player+=1
        r_score.clear()
        r_score.write("PLAYER "+secondplayer+" : {}".format(Second_Player),align='right',font=('Courier',28,'normal'))
        if Second_Player==5:
            r_win.goto(0,200)
            r_win.write("WINNER :"+secondplayer,align='center',font=('Courier',36,'normal'))
            l_win.goto(0,-200)
            l_win.write("LOSER :"+firstplayer,align='center',font=('Courier',36,'normal'))
            #When screen will display the name of winner and loser so In order to hide the movement of ball we uses the below line
            ball.hideturtle()
            #To keep the graphics window open
            input()
            #l_win.goto(0,0)
            #r_win.goto(0,0)
        
    #BAT AND BALL COLLISION
    if((ball.xcor()>365 and ball.xcor()<371) and (ball.ycor()>right_bat.ycor()-60) and (ball.ycor()<right_bat.ycor()+60)):
        ball.setx(360)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if((ball.xcor()<-365 and ball.xcor()>-371) and (ball.ycor()>left_bat.ycor()-60) and (ball.ycor()<left_bat.ycor()+60)):
        ball.setx(-360)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)


#input("Press")#to keep the graphics window open or you can also write

