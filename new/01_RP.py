import RP
LCD = RP.LCD_1inch28()

LCD.fill_rect(0,0,240,40,LCD.yellow)#LCD.red , green ,blue, yellow ,cyan ,white , black
LCD.text("RP2040-LCD-1.28",60,25,LCD.blue)
LCD.show()