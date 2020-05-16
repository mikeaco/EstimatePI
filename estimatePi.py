import random
from graphics import *


test=int(input("Enter number of dots: "))

win = GraphWin("EstimatePi", 500,500)

def estimatePi(dots):
    circle = 0
    total = 0
    for i in range(dots):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        pt = Point(250-(x*250),250+(y*250))
        pt.setFill('blue')
        pt.draw(win)
        if(x**2+y**2<=1):
            circle+=1
        total+=1
    
    return 4*circle/total
            


circ = Circle(Point(250,250),250)
circ.setFill('red')
circ.draw(win)
line1 = Line(Point(250,0),Point(250,500))
line2 = Line(Point(0,250),Point(500,250))   
line1.draw(win)
line2.draw(win)
pi = estimatePi(test)
result = Text(Point(100,100),"Estimated pi: "+str(pi))
result.draw(win)
print(pi)
win.getMouse()
win.close()