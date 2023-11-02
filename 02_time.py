import time
import RP
LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)#亮度~65535

LCD.fill_rect(0,0,240,40,LCD.red)
LCD.text("Now",110,25,LCD.white)
LCD.show()

now = time.localtime()
LCD.text(str(now),0,120,LCD.black)
LCD.show()