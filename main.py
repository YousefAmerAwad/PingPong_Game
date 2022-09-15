import turtle
import functions as funct
import inserts
import move


inserts.wind.listen()                               #tell the window to expect a keyboard input
inserts.wind.onkeypress(move.racket1_up,'w')        #move racket1 up while pressing 'w'
inserts.wind.onkeypress(move.racket1_down,'s')      #move racket1 down while pressing 'w'
inserts.wind.onkeypress(move.racket2_up,'Up')       #move racket2 up while pressing 'Up'
inserts.wind.onkeypress(move.racket2_down,'Down')   #move racket1 down while pressing 'Down'



dx = 0.1       #the change in x-axis
dy = 0.05
#Main Game Loop
while True:
    inserts.wind.update()   #update the screen
    
    inserts.ball.setx(inserts.ball.xcor() + dx)
    inserts.ball.sety(inserts.ball.ycor() + dy)

    #if the ball hit the top border 
    if inserts.ball.ycor() > 240:
        inserts.ball.sety(240)
        dy *= -1

    if inserts.ball.ycor() < -240:
        inserts.ball.sety(-240)
        dy *= -1

    if inserts.ball.xcor() > 300:
        inserts.ball.goto(0,0)
        dx *= -1

    if inserts.ball.xcor() < -300:
        inserts.ball.goto(0,0)
        dx *= -1

    if inserts.racket1.ycor() > 210:
        inserts.racket1.sety(210)

    if inserts.racket2.ycor() > 210:
        inserts.racket2.sety(210)

    if inserts.racket2.ycor() < -210:
        inserts.racket2.sety(-210)

    if inserts.racket1.ycor() < -210:
        inserts.racket1.sety(-210)



    