import turtle
import functions as funct

wind = turtle.Screen()           #insert a window
wind.title('Ping Pong')          #name the game
wind.bgcolor('black')            #provide color to the screen
wind.setup(height=500,width=600) #size of the game pannel
wind.tracer(0)                   #stop the window from updation automatically

racket1 = funct.insert_racket('racket1','blue',-260,0)    #insert the first racket
racket2 = funct.insert_racket('racket2','red',260,0)      #insert the second racket
ball = funct.insert_ball('ball','white')                  #insert the ball