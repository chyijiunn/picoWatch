import time , RP
from machine import Timer
qmi8658=RP.QMI8658()#引入六軸
LCD = RP.LCD_1inch28()
Brightness =15535
        
while True:
    xyz=qmi8658.Read_XYZ()
    LCD.fill(LCD.black)
    LCD.text('X '+str(round(xyz[0],2)),60,100,LCD.white)
    LCD.text('Y '+str(round(xyz[1],2)),60,140,LCD.white)
    LCD.text('Z '+str(round(xyz[2],2)),60,180,LCD.white)

    LCD.text(str(round(xyz[3],2)),125,100,LCD.white)
    LCD.text(str(round(xyz[4],2)),125,140,LCD.white)
    LCD.text(str(round(xyz[5],2)),125,180,LCD.white)

    LCD.show()
    time.sleep(0.1)
