import time
import RP
LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)

LCD.fill_rect(0,0,240,40,LCD.red)
LCD.text("Now",110,25,LCD.white)
LCD.show()
while 1:#重複更新時間，並暫停一秒，這邊的停頓一秒是真的一秒嗎？
    now = list(time.localtime())
    LCD.text(str(now[3:6]),80,120,LCD.black)
    LCD.show()
    time.sleep(1)
