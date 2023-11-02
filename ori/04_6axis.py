from RP import *

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)#亮度~65535
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))

LCD.fill(LCD.black)
LCD.fill_rect(0,0,240,40,LCD.yellow)
LCD.text("MoveMode",85,25,LCD.cyan)

while True:
    LCD.fill(LCD.cyan)
    xyz=qmi8658.Read_XYZ()

    LCD.text("A_X={:+.2f}".format(xyz[0]),20,100-3,LCD.white)
    LCD.text("A_Z={:+.2f}".format(xyz[1]),20,140-3,LCD.white)
    LCD.text("A_Y={:+.2f}".format(xyz[2]),20,180-3,LCD.white)
    
    LCD.text("GYR_X={:+3.2f}".format(xyz[3]),125,100-3,LCD.white)
    LCD.text("GYR_Z={:+3.2f}".format(xyz[4]),125,140-3,LCD.white)
    LCD.text("GYR_Y={:+3.2f}".format(xyz[5]),125,180-3,LCD.white)
    
    LCD.show()
    
    time.sleep(1)
    
