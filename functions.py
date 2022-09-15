import turtle



#insert racket
def insert_racket(name,color,x=0,y=0):
    name = turtle.Turtle()  #insert a turtle object  
    name.shape('square')    #set the shape of the object
    name.speed(0)           #set the speed of the animation
    name.color(color)       #set the color of the object
    name.penup()            #stop the object from drawing lines while moving
    name.goto(x,y)          #set the initial position of the object
    name.shapesize(4,1)     #stretch the object to fit the appropriate size
    return name


#insert ball
def insert_ball(name,color,x=0,y=0):
    name = turtle.Turtle()  #insert a turtle object  
    name.shape('circle')    #set the shape of the object
    name.speed(0)           #set the speed of the animation
    name.color(color)       #set the color of the object
    name.penup()            #stop the object from drawing lines while moving
    name.goto(x,y)          #set the initial position of the object
    return name



