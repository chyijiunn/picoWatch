import time
import RP
LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)

LCD.fill_rect(0,0,240,40,LCD.black)#從 (0,0) 增加長寬 (240,40)
LCD.text("Now",110,25,LCD.white)

now = list(time.gmtime())
LCD.text(str(now[3:6]),80,120,LCD.cyan)#list 3 ~ 6 ，不含 6
LCD.show()

print(now)