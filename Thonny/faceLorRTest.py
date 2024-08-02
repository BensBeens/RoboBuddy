from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time

import machine
import time
import MPU6050
from collections import deque


WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)


# Set up the I2C interface
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))
# Set up the MPU6050 class 
mpu = MPU6050.MPU6050(i2c)
# wake up the MPU6050 from sleep
mpu.wake()
data_queue = []
average = 0


images = []
for n in range(1, 3):
    with open('/faceAnim/face%s.pbm' % n, 'rb') as f:  #open folder and image
        f.readline() # Magic number
        f.readline() # Creator comment
        f.readline() # Dimensions
        data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB) #adjust accordingly the width and height
    images.append(fbuf)

with open('/RoboFaces/faceRight.pbm', 'rb') as R:
    R.readline() # number
    R.readline() # Creator
    R.readline() # Dimensions
    dataR = bytearray(R.read())
    fbuf_R = framebuf.FrameBuffer(dataR, 128, 64, framebuf.MONO_HLSB) #adjust accordingly the width and height
    
with open('/RoboFaces/faceLeft.pbm', 'rb') as L:
    L.readline() # number
    L.readline() # Creator
    L.readline() # Dimensions
    dataL = bytearray(L.read())
    fbuf_L = framebuf.FrameBuffer(dataL, 128, 64, framebuf.MONO_HLSB) #adjust accordingly the width and height
    
while True:
    Ax, Ay, Az = mpu.read_accel_data()
    data_queue.append(Ay)

    if len(data_queue) == 3:
        average = sum(data_queue) / 3
        #print(f"The average of the last 5 inputs is: {average}")
        data_queue.clear()
    time.sleep(0.001)
    
    if -0.5 <= average  <= 0.5:
        for i in images:
            display.blit(i, 0, 0)
            display.show()
            time.sleep(0.3)
    elif average > 0.5:
        display.invert(0)
        display.blit(fbuf_R, 0, 0)
        display.show()
    elif average < -0.5:
        display.invert(0)
        display.blit(fbuf_L, 0, 0)
        display.show()
