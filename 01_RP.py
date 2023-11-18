import RP#引入寫好的
LCD = RP.LCD_1inch28()

LCD.fill_rect(0,0,240,40,LCD.yellow)#畫一個長方形，從0,0開始，大小為240 ,40，並設定顏色LCD.red , green ,blue, yellow ,cyan ,white , black
LCD.text("RP2040-LCD-1.28",60,25,LCD.blue)#寫一個字，位置是110,25,顏色是白色
LCD.show()#讓上面呈現出來