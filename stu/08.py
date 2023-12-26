import touch,time
LCD = touch.LCD_1inch28()
LCD.set_bl_pwm(15535)#設定亮度~65535

LCD.fill(LCD.black)
LCD.fill_rect(0,0,240,40,LCD.green)

LCD.write_text(str(time.localtime()[0]),75,35,3,LCD.color(255,125,100))
LCD.write_text(str(time.localtime()[1])+'/'+str(time.localtime()[2]),60,65,3,LCD.color(255,255,100))

while 1:
    for i in range(3,6):
        LCD.write_text(str(time.localtime()[i]),100,i*30+35,3,LCD.color(255,4*int(time.localtime()[i]),215))
    LCD.show()
    LCD.fill_rect(100,125,50,90,LCD.color(0,0,0))