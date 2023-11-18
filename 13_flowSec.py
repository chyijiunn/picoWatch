import time , RP, math
qmi8658=RP.QMI8658()#讀取六軸資料
LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)
cx , cy =120 ,120 #center of watch

def spin( tic , spinLen , color):
    now = list(time.localtime())
    x = spinLen*math.sin(math.radians(now[tic]*6))
    y = spinLen*math.cos(math.radians(now[tic]*6))
    LCD.line(cx,cy,int(cx+x),int(cy-y),color)
    
def hourspin(spinLen , color):
    now = list(time.localtime())
    
    if now[3] < 12:hh = now[3]#切換24小時制 --> 12 小時制
    else : hh = now[3] - 12
    
    x = spinLen*math.sin(math.radians(hh*30+(now[4]/2))) #hour spin 30˚/h , +0.5˚/min
    y = spinLen*math.cos(math.radians(hh*30+(now[4]/2)))
    LCD.line(cx,cy,int(cx+x),int(cy-y),color)

def centerCircle(tic , spinLen , color):
    now = list(time.localtime())
    r = now[tic]*2
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(cx+i,cy+j,color)
                
def runDotRing(tic , spinLen , color):
    xyz=qmi8658.Read_XYZ()
    x = int(spinLen*xyz[0])
    z = int(spinLen*xyz[1])
    
    print(x ,z)
    r = 10
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(cx+z+i,cy-x+j,color)

def runDotFlow(tic , spinLen , color):
    xyz=qmi8658.Read_XYZ()
    x = int(spinLen*xyz[0])
    z = int(spinLen*xyz[1])
    
    print(x ,z)
    r = 10
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(cx+z+i,cy-x+j,color)
                
while 1:
    LCD.fill_rect(0,00,240,240,LCD.white)#全螢幕刷新
    '''
    spin(5,120,LCD.red)
    spin(4,100,LCD.black)
    hourspin(50 ,LCD.cyan )
    '''
    runDotRing(5,110,LCD.red)
    LCD.show()
    time.sleep(0.05)



