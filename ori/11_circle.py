from RP import *
from time import sleep
import math , random
randomColor = random.randint(-1,256)
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

for p in range(0,360,1):
    hxn, hyn = end_point(p, 120)
    LCD.line(120,120,120+hxn,120+hyn,color(randomColor,random.randint(-1,256),randomColor+p))
    r = 30
    LCD.show()
    #sleep(0.1)
