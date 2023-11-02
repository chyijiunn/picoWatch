from RP import *

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)#亮度~65535
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))

LCD.fill(LCD.black)
LCD.fill_rect(0,0,240,40,LCD.yellow)
LCD.text("Trunking",80,25,LCD.cyan)

nowtime = utime.localtime()
print(nowtime)

LCD.text(str(nowtime[0]),90,100,LCD.white)
LCD.text(str(nowtime[1]),130,100,LCD.white)
LCD.text(str(nowtime[2]),145,100,LCD.white)

while True:
    nowtime = utime.localtime()
    LCD.text(str(nowtime[3]),100,125,LCD.white)
    LCD.text(str(nowtime[4]),120,125,LCD.white)
    LCD.text(str(nowtime[5]),140,125,LCD.white)
    
    LCD.show()
    time.sleep(1)
    LCD.fill_rect(100,125,200,200,LCD.black)
    LCD.show()

