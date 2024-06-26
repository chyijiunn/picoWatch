import touch,time,math
LCD = touch.LCD_1inch28()
LCD.set_bl_pwm(15535)#設定亮度~65535

LCD.fill(LCD.black)
LCD.fill_rect(0,0,240,40,LCD.black)

while True:
    LCD.write_text(str(time.localtime()[0]),80,35,3,LCD.color(25,125,125))
    LCD.write_text(str(time.localtime()[1])+'/'+str(time.localtime()[2]),90,65,3,LCD.color(125,125,225))

    LCD.write_text(str(time.localtime()[3])+':'+str(time.localtime()[4]),20,100,5,LCD.color(125,225,125))
    LCD.write_text(str(time.localtime()[5]),100,160,7,LCD.color(225,125,60+2*int(time.localtime()[5])))
    
    radian = math.radians(time.localtime()[5]*6)
    x_sin = math.sin(radian)
    y_cos = math.cos(radian)
    x = int(90*x_sin+120)
    y = int(-90*y_cos+120)
    
    LCD.pixel(x+15,y+6,LCD.color(251,86,7))
    LCD.pixel(x+14,y+7,LCD.color(251,86,7))
    LCD.pixel(x+15,y+7,LCD.color(255,190,11))
    LCD.pixel(x+16,y+7,LCD.color(251,86,7))
    LCD.pixel(x+14,y+8,LCD.color(251,86,7))
    LCD.pixel(x+15,y+8,LCD.color(255,190,11))
    LCD.pixel(x+16,y+8,LCD.color(251,86,7))
    LCD.pixel(x+13,y+9,LCD.color(251,86,7))
    LCD.pixel(x+14,y+9,LCD.color(255,190,11))
    LCD.pixel(x+15,y+9,LCD.color(255,190,11))
    LCD.pixel(x+16,y+9,LCD.color(255,190,11))
    LCD.pixel(x+17,y+9,LCD.color(251,86,7))
    LCD.pixel(x+13,y+10,LCD.color(251,86,7))
    LCD.pixel(x+14,y+10,LCD.color(255,190,11))
    LCD.pixel(x+15,y+10,LCD.color(255,190,11))
    LCD.pixel(x+16,y+10,LCD.color(255,190,11))
    LCD.pixel(x+17,y+10,LCD.color(251,86,7))
    LCD.pixel(x+12,y+11,LCD.color(251,86,7))
    LCD.pixel(x+13,y+11,LCD.color(251,86,7))
    LCD.pixel(x+14,y+11,LCD.color(255,190,11))
    LCD.pixel(x+15,y+11,LCD.color(255,190,11))
    LCD.pixel(x+16,y+11,LCD.color(255,190,11))
    LCD.pixel(x+17,y+11,LCD.color(255,190,11))
    LCD.pixel(x+18,y+11,LCD.color(251,86,7))
    LCD.pixel(x+7,y+12,LCD.color(251,86,7))
    LCD.pixel(x+8,y+12,LCD.color(251,86,7))
    LCD.pixel(x+9,y+12,LCD.color(251,86,7))
    LCD.pixel(x+10,y+12,LCD.color(251,86,7))
    LCD.pixel(x+11,y+12,LCD.color(251,86,7))
    LCD.pixel(x+12,y+12,LCD.color(251,86,7))
    LCD.pixel(x+13,y+12,LCD.color(255,190,11))
    LCD.pixel(x+14,y+12,LCD.color(255,190,11))
    LCD.pixel(x+15,y+12,LCD.color(255,190,11))
    LCD.pixel(x+16,y+12,LCD.color(255,190,11))
    LCD.pixel(x+17,y+12,LCD.color(255,190,11))
    LCD.pixel(x+18,y+12,LCD.color(251,86,7))
    LCD.pixel(x+19,y+12,LCD.color(251,86,7))
    LCD.pixel(x+20,y+12,LCD.color(251,86,7))
    LCD.pixel(x+21,y+12,LCD.color(251,86,7))
    LCD.pixel(x+22,y+12,LCD.color(251,86,7))
    LCD.pixel(x+23,y+12,LCD.color(251,86,7))
    LCD.pixel(x+8,y+13,LCD.color(251,86,7))
    LCD.pixel(x+9,y+13,LCD.color(255,190,11))
    LCD.pixel(x+10,y+13,LCD.color(255,190,11))
    LCD.pixel(x+11,y+13,LCD.color(255,190,11))
    LCD.pixel(x+12,y+13,LCD.color(255,190,11))
    LCD.pixel(x+13,y+13,LCD.color(52,58,64))
    LCD.pixel(x+14,y+13,LCD.color(255,190,11))
    LCD.pixel(x+15,y+13,LCD.color(255,190,11))
    LCD.pixel(x+16,y+13,LCD.color(255,190,11))
    LCD.pixel(x+17,y+13,LCD.color(52,58,64))
    LCD.pixel(x+18,y+13,LCD.color(255,190,11))
    LCD.pixel(x+19,y+13,LCD.color(255,190,11))
    LCD.pixel(x+20,y+13,LCD.color(255,190,11))
    LCD.pixel(x+21,y+13,LCD.color(255,190,11))
    LCD.pixel(x+22,y+13,LCD.color(251,86,7))
    LCD.pixel(x+9,y+14,LCD.color(251,86,7))
    LCD.pixel(x+10,y+14,LCD.color(255,190,11))
    LCD.pixel(x+11,y+14,LCD.color(255,190,11))
    LCD.pixel(x+12,y+14,LCD.color(255,190,11))
    LCD.pixel(x+13,y+14,LCD.color(52,58,64))
    LCD.pixel(x+14,y+14,LCD.color(255,190,11))
    LCD.pixel(x+15,y+14,LCD.color(255,190,11))
    LCD.pixel(x+16,y+14,LCD.color(255,190,11))
    LCD.pixel(x+17,y+14,LCD.color(52,58,64))
    LCD.pixel(x+18,y+14,LCD.color(255,190,11))
    LCD.pixel(x+19,y+14,LCD.color(255,190,11))
    LCD.pixel(x+20,y+14,LCD.color(255,190,11))
    LCD.pixel(x+21,y+14,LCD.color(251,86,7))
    LCD.pixel(x+10,y+15,LCD.color(251,86,7))
    LCD.pixel(x+11,y+15,LCD.color(255,190,11))
    LCD.pixel(x+12,y+15,LCD.color(255,190,11))
    LCD.pixel(x+13,y+15,LCD.color(52,58,64))
    LCD.pixel(x+14,y+15,LCD.color(255,190,11))
    LCD.pixel(x+15,y+15,LCD.color(255,190,11))
    LCD.pixel(x+16,y+15,LCD.color(255,190,11))
    LCD.pixel(x+17,y+15,LCD.color(52,58,64))
    LCD.pixel(x+18,y+15,LCD.color(255,190,11))
    LCD.pixel(x+19,y+15,LCD.color(255,190,11))
    LCD.pixel(x+20,y+15,LCD.color(251,86,7))
    LCD.pixel(x+11,y+16,LCD.color(251,86,7))
    LCD.pixel(x+12,y+16,LCD.color(255,190,11))
    LCD.pixel(x+13,y+16,LCD.color(255,190,11))
    LCD.pixel(x+14,y+16,LCD.color(255,190,11))
    LCD.pixel(x+15,y+16,LCD.color(255,190,11))
    LCD.pixel(x+16,y+16,LCD.color(255,190,11))
    LCD.pixel(x+17,y+16,LCD.color(255,190,11))
    LCD.pixel(x+18,y+16,LCD.color(255,190,11))
    LCD.pixel(x+19,y+16,LCD.color(251,86,7))
    LCD.pixel(x+12,y+17,LCD.color(251,86,7))
    LCD.pixel(x+13,y+17,LCD.color(255,190,11))
    LCD.pixel(x+14,y+17,LCD.color(255,190,11))
    LCD.pixel(x+15,y+17,LCD.color(255,190,11))
    LCD.pixel(x+16,y+17,LCD.color(255,190,11))
    LCD.pixel(x+17,y+17,LCD.color(255,190,11))
    LCD.pixel(x+18,y+17,LCD.color(251,86,7))
    LCD.pixel(x+11,y+18,LCD.color(251,86,7))
    LCD.pixel(x+12,y+18,LCD.color(255,190,11))
    LCD.pixel(x+13,y+18,LCD.color(255,190,11))
    LCD.pixel(x+14,y+18,LCD.color(255,190,11))
    LCD.pixel(x+15,y+18,LCD.color(255,190,11))
    LCD.pixel(x+16,y+18,LCD.color(255,190,11))
    LCD.pixel(x+17,y+18,LCD.color(255,190,11))
    LCD.pixel(x+18,y+18,LCD.color(255,190,11))
    LCD.pixel(x+19,y+18,LCD.color(251,86,7))
    LCD.pixel(x+10,y+19,LCD.color(251,86,7))
    LCD.pixel(x+11,y+19,LCD.color(255,190,11))
    LCD.pixel(x+12,y+19,LCD.color(255,190,11))
    LCD.pixel(x+13,y+19,LCD.color(255,190,11))
    LCD.pixel(x+14,y+19,LCD.color(255,190,11))
    LCD.pixel(x+15,y+19,LCD.color(255,190,11))
    LCD.pixel(x+16,y+19,LCD.color(255,190,11))
    LCD.pixel(x+17,y+19,LCD.color(255,190,11))
    LCD.pixel(x+18,y+19,LCD.color(255,190,11))
    LCD.pixel(x+19,y+19,LCD.color(255,190,11))
    LCD.pixel(x+20,y+19,LCD.color(251,86,7))
    LCD.pixel(x+9,y+20,LCD.color(251,86,7))
    LCD.pixel(x+10,y+20,LCD.color(255,190,11))
    LCD.pixel(x+11,y+20,LCD.color(255,190,11))
    LCD.pixel(x+12,y+20,LCD.color(255,190,11))
    LCD.pixel(x+13,y+20,LCD.color(251,86,7))
    LCD.pixel(x+14,y+20,LCD.color(251,86,7))
    LCD.pixel(x+15,y+20,LCD.color(251,86,7))
    LCD.pixel(x+16,y+20,LCD.color(251,86,7))
    LCD.pixel(x+17,y+20,LCD.color(251,86,7))
    LCD.pixel(x+18,y+20,LCD.color(255,190,11))
    LCD.pixel(x+19,y+20,LCD.color(255,190,11))
    LCD.pixel(x+20,y+20,LCD.color(255,190,11))
    LCD.pixel(x+21,y+20,LCD.color(251,86,7))
    LCD.pixel(x+8,y+21,LCD.color(251,86,7))
    LCD.pixel(x+9,y+21,LCD.color(255,190,11))
    LCD.pixel(x+10,y+21,LCD.color(251,86,7))
    LCD.pixel(x+11,y+21,LCD.color(251,86,7))
    LCD.pixel(x+12,y+21,LCD.color(251,86,7))
    LCD.pixel(x+13,y+21,LCD.color(251,86,7))
    LCD.pixel(x+17,y+21,LCD.color(251,86,7))
    LCD.pixel(x+18,y+21,LCD.color(251,86,7))
    LCD.pixel(x+19,y+21,LCD.color(251,86,7))
    LCD.pixel(x+20,y+21,LCD.color(251,86,7))
    LCD.pixel(x+21,y+21,LCD.color(255,190,11))
    LCD.pixel(x+22,y+21,LCD.color(251,86,7))
    LCD.pixel(x+7,y+22,LCD.color(251,86,7))
    LCD.pixel(x+8,y+22,LCD.color(251,86,7))
    LCD.pixel(x+9,y+22,LCD.color(251,86,7))
    LCD.pixel(x+10,y+22,LCD.color(251,86,7))
    LCD.pixel(x+20,y+22,LCD.color(251,86,7))
    LCD.pixel(x+21,y+22,LCD.color(251,86,7))
    LCD.pixel(x+22,y+22,LCD.color(251,86,7))
    LCD.pixel(x+23,y+22,LCD.color(251,86,7))

    LCD.show()
    LCD.fill_rect(0,0,240,240,LCD.black)
