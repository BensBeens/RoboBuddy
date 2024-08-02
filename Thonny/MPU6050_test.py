import machine
import time
import MPU6050
from collections import deque

# Set up the I2C interface
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))

# Set up the MPU6050 class 
mpu = MPU6050.MPU6050(i2c)

# wake up the MPU6050 from sleep
mpu.wake()

data_queue = []

# continuously print the data
while True:
    Gx, Gy, Gz = mpu.read_gyro_data()
    Ax, Ay, Az = mpu.read_accel_data()
    #print("Gyro: " + str(gyro) + ", Accel: " + str(accel))
    
    data_queue.append(Ay)
    if len(data_queue) == 5:
        average = sum(data_queue) / 5
        print(f"The average of the last 5 inputs is: {average}")
        data_queue.clear()
    
#     print ("Gyro: " + str(Gx))
    time.sleep(0.01)

