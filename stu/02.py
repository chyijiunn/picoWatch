import touch,time
LCD = touch.LCD_1inch28()
LCD.set_bl_pwm(15535)#設定亮度~65535

LCD.fill_rect(0,0,240,40,LCD.green)

LCD.text("Now",90,25,LCD.black)
LCD.write_text("Now",90,55,2,LCD.black)
LCD.write_text("Now",90,85,3,LCD.black)
LCD.write_text("Now",90,115,4,LCD.black)
LCD.write_text("Now",90,145,5,LCD.black)

LCD.show()