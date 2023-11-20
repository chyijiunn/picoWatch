import RP#引入寫好的
LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(15535)#設定亮度~65535

LCD.fill_rect(0,0,240,40,LCD.green)#畫一個長方形，從0,0開始，大小為240 ,40，並設定顏色LCD.red , green ,blue, yellow ,cyan ,white , black
LCD.text("Trunking",90,25,LCD.black)#寫一個字，位置是110,25,顏色是黑色
LCD.show()#讓上面呈現出來