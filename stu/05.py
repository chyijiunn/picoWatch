import touch,time
LCD = touch.LCD_1inch28()
LCD.set_bl_pwm(15535)#設定亮度~65535

LCD.fill(LCD.black)
LCD.fill_rect(0,0,240,40,LCD.green)

for i in range(6):
    LCD.write_text(str(time.localtime()[i]),80,i*30+35,3,LCD.color(255,100+i*30,100))
    
LCD.show()