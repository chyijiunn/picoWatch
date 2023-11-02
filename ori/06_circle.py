from RP import *

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)#亮度~65535

LCD.fill(LCD.cyan)
LCD.fill_rect(0,0,240,40,LCD.yellow)
r = 30
for i in range(-r,r,1):
    for j in range(-r,r,1):
        if i*i + j*j <= r*r:
            LCD.pixel(120+i,120+j,LCD.white)
    
LCD.show()


