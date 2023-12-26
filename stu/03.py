import touch,time
LCD = touch.LCD_1inch28()
LCD.set_bl_pwm(15535)#設定亮度~65535

LCD.fill_rect(0,0,240,40,LCD.green)
LCD.write_text(str(time.localtime()[0]),60,25,4,LCD.black)
LCD.show()