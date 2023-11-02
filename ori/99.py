from RP import *

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)#亮度~65535
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))

r = 10
ori_x = 120
ori_z = 10
while True:
    LCD.fill(LCD.cyan)
    xyz=qmi8658.Read_XYZ()
    x_shift = int(xyz[3])
    z_shift = int(xyz[4])
    if ((ori_x - 120)*(ori_x - 120))+ ((ori_z - 120)*(ori_z - 120)) ==110*110:
        after_x = ori_x
        after_z = ori_z
        for i in range(-r,r,1):
            for j in range(-r,r,1):
                if i*i + j*j <= r*r:
                    LCD.pixel(after_x+i-x_shift,after_z+j-z_shift,LCD.white)
        ori_x = after_x - x_shift
        ori_z = after_z - z_shift
        if   ori_x >= 240:ori_x=240
        if   ori_x <= 0:ori_x=0
        if   ori_z >= 240:ori_z=240
        if   ori_z <= 0:ori_z=0
    LCD.show()
