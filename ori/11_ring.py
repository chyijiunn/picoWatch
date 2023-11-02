from RP import *
from time import sleep
import math

LCD = LCD_1inch28()
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))
def color(R,G,B):
    return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)

def end_point(theta, rr):                       
    theta_rad = math.radians(theta)    
    xx = int(rr * math.sin(theta_rad))
    yy = -int(rr * math.cos(theta_rad))                     
    return xx,yy

class Point:
    def __init__(self,x,y):
        self.X=x
        self.Y=y
    def __str__(self):
        return "Point(%s,%s)"%(self.X,self.Y)
        
class Triangle:
    def __init__(self,p1,p2,p3):
        self.P1=p1
        self.P2=p2
        self.P3=p3

    def __str__(self):
        return "Triangle(%s,%s,%s)"%(self.P1,self.P2,self.P3)
    
    def draw(self):
        print("I should draw now")
        self.fillTri()
    # Filled triangle routines ported from http://www.sunshine2k.de/coding/java/TriangleRasterization/TriangleRasterization.html      
    def sortVerticesAscendingByY(self):    
        if self.P1.Y > self.P2.Y:
            vTmp = self.P1
            self.P1 = self.P2
            self.P2 = vTmp
        
        if self.P1.Y > self.P3.Y:
            vTmp = self.P1
            self.P1 = self.P3
            self.P3 = vTmp

        if self.P2.Y > self.P3.Y:
            vTmp = self.P2
            self.P2 = self.P3
            self.P3 = vTmp
        
    def fillTri(self):
        self.sortVerticesAscendingByY()
        if self.P2.Y == self.P3.Y:
            fillBottomFlatTriangle(self.P1, self.P2, self.P3)
        else:
            if self.P1.Y == self.P2.Y:
                fillTopFlatTriangle(self.P1, self.P2, self.P3)
            else:
                newx = int(self.P1.X + (float(self.P2.Y - self.P1.Y) / float(self.P3.Y - self.P1.Y)) * (self.P3.X - self.P1.X))
                newy = self.P2.Y                
                pTmp = Point( newx,newy )
#                print(pTmp)
                fillBottomFlatTriangle(self.P1, self.P2, pTmp)
                fillTopFlatTriangle(self.P2, pTmp, self.P3)

def fillBottomFlatTriangle(p1,p2,p3):
#    print("BF",p1,p2,p3)
    if p2.Y > p3.Y:
        ty = p3.Y
        p3.Y = p2.Y
        p2.Y = ty
        tx = p3.X
        p3.X = p2.X
        p2.X = tx
        print(p1,p2,p3)
    
    slope1 = float(p2.X - p1.X) / float (p2.Y - p1.Y)
    slope2 = float(p3.X - p1.X) / float (p3.Y - p1.Y)

    x1 = p1.X
    x2 = p1.X + 0.5
#    print("B",p1.Y,p2.Y)
    for scanlineY in range(p1.Y,p2.Y):
#        print(scanlineY)
#        LCD.pixel_span(int(x1), scanlineY, int(x2)-int(x1))   # Switch pixel_span() to hline() / Pimoroni to WS
        LCD.hline(int(x1),scanlineY, int(x2)-int(x1),c)        
        LCD.hline(int(x2),scanlineY, -(int(x2)-int(x1)),c)
#        LCD.show()          #                  Here and below        
#        utime.sleep(0.1)    #     <===== Uncomment to see how graphic elements are drawn
        x1 += slope1
        x2 += slope2
#    LCD.show()              #                  LCD.show() and utime.sleep(0.1)
def fillTopFlatTriangle(p1,p2,p3):
#    print("TF",p1,p2,p3)
    slope1 = float(p3.X - p1.X) / float(p3.Y - p1.Y)
    slope2 = float(p3.X - p2.X) / float(p3.Y - p2.Y)

    x1 = p3.X
    x2 = p3.X + 0.5
#    print("T",p3.Y,p1.Y-1)
    for scanlineY in range (p3.Y,p1.Y-1,-1):
#        print(scanlineY)
#        LCD.pixel_span(int(x1), scanlineY, int(x2)-int(x1))  # Switch pixel_span() to hline() / Pimoroni to WS
        LCD.hline(int(x1),scanlineY, int(x2)-int(x1)+1,c)        
        LCD.hline(int(x2),scanlineY, -(int(x2)-int(x1)-1),c)
#        LCD.show()
#        utime.sleep(0.1)
        x1 -= slope1
        x2 -= slope2
def tri_filled(x1,y1,x2,y2,x3,y3,c): # Draw filled triangle
    t=Triangle(Point(x1,y1),Point(x2,y2),Point(x3,y3))
    t.fillTri() 
for p in range(0,360,6):
    hxn, hyn = end_point(p, 120)
    hxnn , hynn = end_point(p+6, 120)
    #LCD.line(120,120,120+hxn,120+hyn,color(251, 96, 127))
    tri_filled(120,120,120+hxn,120+hyn,120+hxnn,120+hynn,color(251, 96, 127))
    LCD.show()
    sleep(0.1)
