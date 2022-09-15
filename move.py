import inserts

#move racket1 up
def racket1_up():    
    inserts.racket1.sety(inserts.racket1.ycor() + 10)   #increase the y-coordinate of racket1 by 10

#move racket1 down
def racket1_down():    
    inserts.racket1.sety(inserts.racket1.ycor() - 10)   #decrease the y-coordinate of racket1 by 10

#move racket2 up
def racket2_up():    
    inserts.racket2.sety(inserts.racket2.ycor() + 10)   #increase the y-coordinate of racket2 by 10

#move racket2 down
def racket2_down():    
    inserts.racket2.sety(inserts.racket2.ycor() - 10)   #decrease the y-coordinate of racket2 by 10