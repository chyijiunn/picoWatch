import time
import RP
LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)#設定亮度~65535

LCD.fill_rect(0,0,240,40,LCD.red)
LCD.text("Now",110,25,LCD.white)
LCD.show()#讓上面的呈現出來

now = time.localtime()#讀取機器內時間
LCD.text(str(now),0,120,LCD.black)#把剛剛時間寫入LCD
LCD.show()