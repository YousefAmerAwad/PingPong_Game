import turtle
import functions as funct

wind = turtle.Screen()           #insert a window
wind.title('Ping Pong')          #name the game
wind.bgcolor('black')            #provide color to the screen
wind.setup(height=500,width=500) #size of the game pannel
wind.tracer(0)                   #stop the window from updation automatically

funct.insert_racket('racket1','blue',-210,0)    #insert the first racket
funct.insert_racket('racket2','red',210,0)      #insert the second racket
funct.insert_ball('ball','white')               #insert the ball


#Main Game Loop
while True:
    wind.update()   #update the screen


