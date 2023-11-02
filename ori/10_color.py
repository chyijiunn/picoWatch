from RP import *
LCD = LCD_1inch28()
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))




def color(R,G,B): # Convert RGB888 to RGB565
    return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)
print(color(0, 177, 112))
#LCD.fill(color(0, 177, 112))
LCD.fill(36357)
LCD.show()
