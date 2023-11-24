from RP import *
LCD = LCD_1inch28()
LCD.set_bl_pwm(15535)

def color(R,G,B): #  RGB888 to RGB565
    return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)

# https://coolors.co/generate，改一下(R,G,B)
convert = color(237, 40, 201)
print(convert)
LCD.fill(convert)
LCD.show()

LCD.fill_rect(20,20,80,80,0)
LCD.show()
for i in range(50):
    LCD.scroll(2,2)#以整個畫面為單位，每次位移 x , y 都 +2
    time.sleep(0.01)
    LCD.show()


