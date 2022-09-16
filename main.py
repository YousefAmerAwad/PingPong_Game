import turtle
import functions as funct
import inserts
import move


inserts.wind.listen()                               #tell the window to expect a keyboard input
inserts.wind.onkeypress(move.racket1_up,'w')        #move racket1 up while pressing 'w'
inserts.wind.onkeypress(move.racket1_down,'s')      #move racket1 down while pressing 'w'
inserts.wind.onkeypress(move.racket2_up,'Up')       #move racket2 up while pressing 'Up'
inserts.wind.onkeypress(move.racket2_down,'Down')   #move racket1 down while pressing 'Down'

score1 = 0
score2 = 0
score = turtle.Turtle()
score.color('white')
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0,220)
score.write('Player1: 0        Player2: 0',align='center',font=('courier',20,'normal'))


dx = 0.07       #the change in x-axis
dy = 0.04
#Main Game Loop
while True:
    inserts.wind.update()   #update the screen
    
    inserts.ball.setx(inserts.ball.xcor() + dx)
    inserts.ball.sety(inserts.ball.ycor() + dy)



    if inserts.ball.ycor() > 240:   #if the ball hits the upper border
        inserts.ball.sety(240)      #let it bounce
        dy *= -1     

    
    if inserts.ball.ycor() < -240:   #if the ball hits the bottom
        inserts.ball.sety(-240)      #let it will bounce 
        dy *= -1       

    if inserts.ball.xcor() > 300:    #if the ball hits the right border
        inserts.ball.goto(0,0)       #return it back to the center
        score1+=1
        score.clear()
        score.write('Player1: {}        Player2: {} '.format(score1,score2),align='center',font=('courier',20,'normal'))
        dx *= -1                     #reverse it's direction

    if inserts.ball.xcor() < -300:   #if the ball hits the left border  
        inserts.ball.goto(0,0)       #return it back to the center
        score2+=1
        score.clear()
        score.write('Player1: {}        Player2: {} '.format(score1,score2),align='center',font=('courier',20,'normal'))
        dx *= -1                     #reverse it's direction

    if inserts.racket1.ycor() > 210: #if the racket1 hits the upper border
        inserts.racket1.sety(210)    #don't let it cross the border

    if inserts.racket2.ycor() > 210:
        inserts.racket2.sety(210)

    if inserts.racket2.ycor() < -210:
        inserts.racket2.sety(-210)

    if inserts.racket1.ycor() < -210:
        inserts.racket1.sety(-210)

    if (inserts.ball.xcor() > 250 and inserts.ball.xcor() < 260) and (inserts.ball.ycor() < inserts.racket2.ycor() + 50 and inserts.ball.ycor() > inserts.racket2.ycor() - 50):
        inserts.ball.setx(240)
        dx *= -1

    if (inserts.ball.xcor() < -250 and inserts.ball.xcor() > -260) and (inserts.ball.ycor() < inserts.racket1.ycor() + 50 and inserts.ball.ycor() > inserts.racket1.ycor() - 50):
        inserts.ball.setx(-240)
        dx *= -1




    