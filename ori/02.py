from RP import *

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)#亮度~65535
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))

LCD.fill(LCD.black)
LCD.fill_rect(0,40,240,40,LCD.yellow)
LCD.text("Trunking",80,25,LCD.cyan)
LCD.show()