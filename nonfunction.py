from math import *
from Graphics import *

#Viewport Range
minX = -30
maxX = 30
minY = -30
maxY = 30

#Tolerance for each value (larger -- less tolerant) DEFAULT 400
tolerance = 300

#Step size (larger takes LONGER) DEFAULT 1280
accuracy = 1280


win = Window(320,320)
blankPic = Picture(320, 320)

def graphIt():
    X = minX
    Y = minY



    while (X < maxX):
            while(Y < maxY):
                if(f(X, Y) == True):
                    setPixel(blankPic, (int(X * (640 / (maxX - minX)))), (int(Y * (640 / (maxY - minY)))), Color("Black"))                   
                Y += (fabs(maxY - minY) / accuracy)
            Y = minY
            X += (fabs(maxX - minX) / accuracy)    
        
            
       # print(int(X * (640 / (maxX - minX))))           
    

    
def f(X, Y):
    
   upperLimit1 = R(X + (fabs(maxX - minX) / tolerance), Y + (fabs(maxY - minY) / tolerance))
   lowerLimit1 = R(X - (fabs(maxX - minX) / tolerance), Y - (fabs(maxY - minY) / tolerance))
   upperLimit2 = R(X - (fabs(maxX - minX) / tolerance), Y + (fabs(maxY - minY) / tolerance))
   lowerLimit2 = R(X + (fabs(maxX - minX) / tolerance), Y - (fabs(maxY - minY) / tolerance))
    
    
   if (((lowerLimit1 <= L(X, Y)) and (L(X, Y) <= upperLimit1)) or ((upperLimit1 <= L(X, Y)) and (L(X, Y) <= lowerLimit1))):
        return True
        
   elif (((lowerLimit2 <= L(X, Y)) and (L(X, Y) <= upperLimit2)) or ((upperLimit2 <= L(X, Y)) and (L(X, Y) <= lowerLimit2))):
        return True
        
   else:
       return False
 

def R(X, Y):
    return -X * sin(X)
    
def L(X, Y):
    return Y * sin(Y)


    
graphIt()

blankPic.draw(win)
print("done")
