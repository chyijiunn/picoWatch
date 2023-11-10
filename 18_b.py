from machine import Pin,I2C,SPI,PWM,ADC
import RP,framebuf

LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(35535)

fbuf = framebuf.FrameBuffer(bytearray(100 * 10 * 2), 100, 10, framebuf.RGB565)

fbuf.fill(1)
fbuf.text('MicroPython!', 0, 0, 0xffff)
fbuf.hline(0, 20, 96, 0xffff)

LCD.blit(fbuf,60,60)
LCD.show()