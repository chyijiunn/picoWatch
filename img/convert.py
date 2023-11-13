from RP import *
import framebuf
class LCD_1inch28(framebuf.FrameBuffer):
    # ... (之前的代码)

    def display_hex_color_image(self, hex_data):
        try:
            # 转换16进制数据为字节数组
            image_data = bytes.fromhex(hex_data)

            # 创建framebuf对象
            img = framebuf.FrameBuffer(image_data, self.width, self.height, framebuf.RGB565)

            # 清空屏幕
            self.fill(0)

            # 在LCD上显示图像
            self.blit(img, 0, 0)
            self.show()
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    LCD = LCD_1inch28()
    LCD.set_bl_pwm(65535)

    # 替换为你的彩色图像的16进制数据
    hex_data = "..."  

    while True:
        LCD.display_hex_color_image(hex_data)
        time.sleep(2)  # 你可以根据需要调整显示时间间隔
