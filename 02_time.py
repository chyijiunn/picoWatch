import time
import RP
LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)#設定亮度~65535

LCD.fill_rect(0,0,240,40,LCD.red)#畫一個長方形，從0,0開始，大小為240 ,40
LCD.text("Now",110,25,LCD.white)#寫一個字，位置是110,25,顏色是白色
LCD.show()#讓上面的呈現出來

now = time.localtime()#讀取機器內時間
LCD.text(str(now),0,120,LCD.black)#把剛剛時間寫入LCD
LCD.show()