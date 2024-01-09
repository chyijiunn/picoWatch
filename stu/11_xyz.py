import touch,time
LCD = touch.LCD_1inch28()
LCD.set_bl_pwm(15535)#設定亮度~65535

LCD.fill(LCD.black)
LCD.fill_rect(0,0,240,40,LCD.black)

while True:
    xyz=touch.QMI8658().Read_XYZ()
    x = int(120*xyz[1])
    y = int(120*xyz[0])
    
    if x>= 0 :LCD.fill_rect(120,120,x,20,LCD.red)
    else :
        LCD.fill_rect(0,120,120,20,LCD.red)
        LCD.fill_rect(0,120,120+x,20,LCD.black)
    
    if y>= 0 :
        LCD.fill_rect(120,0,20,120,LCD.white)
        LCD.fill_rect(120,0,20,120-y,LCD.black)
    else :LCD.fill_rect(120,120,20,-y,LCD.white)
    
    LCD.fill_rect(120,120,x,20,LCD.red)
    
    
    LCD.show()
    LCD.fill_rect(0,0,240,240,LCD.black)