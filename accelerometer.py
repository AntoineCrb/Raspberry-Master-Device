import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from mpu6050 import mpu6050
from pynput import keyboard
import scipy.integrate as integrate
import time

plt.style.use('ggplot')

accel_X = []
accel_Y = []
accel_Z = []
avg_x = 0
avg_y = 0
avg_z = 0
accel_time = []

mpu = mpu6050(0x68)

def init():
    print("--- initialisation")
    mpu.set_accel_range(mpu.ACCEL_RANGE_2G)
    mpu.set_gyro_range(mpu.GYRO_RANGE_250DEG)

def get_accel():
    ac_data = mpu.get_accel_data()
    accel_time.append(time.time())
    accel_X.append(ac_data['x'])
    accel_Y.append(ac_data['y'])
    accel_Z.append(ac_data['z'])

def update_time():
    for k in range(1, len(accel_time)):
        accel_time[k] -= accel_time[0]

def reset_offset_accel():
    global avg_x, avg_y, avg_z, accel_X, accel_Y, accel_Z, accel_time
    avg_x = np.mean(accel_X[5:])
    avg_y = np.mean(accel_Y[5:])
    avg_z = np.mean(accel_Z[5:])
    accel_X = []
    accel_Y = []
    accel_Z = []
    accel_time = []

def update_accel():
    for k in range(len(accel_X)):
        accel_X[k] -= avg_x
    for k in range(len(accel_Y)):
        accel_Y[k] -= avg_y
    for k in range(len(accel_Z)):
        accel_Z[k] -= avg_z

def run():
    print("running...")
    init()
    print("start getting offset...")
    start = time.time()
    while time.time() - start < 5:
        get_accel()
    reset_offset_accel()
    start = time.time()
    print("start real measure...")
    while time.time() - start < 10:
        get_accel()
    print("printing graph...")
    update_time()
    update_accel()
    fig, axs = plt.subplots(3, 2)

    axs[0, 0].plot(accel_time[5:], accel_X[5:])
    axs[0, 0].set_title('accel X')
    axs[0, 1].plot(accel_time[5:], integrate.cumtrapz(accel_X[5:], accel_time[5:], initial=0))
    axs[0, 1].set_title('speed X')

    axs[1, 0].plot(accel_time[5:], accel_Y[5:], 'tab:orange')
    axs[1, 0].set_title('accel Y')
    axs[1, 1].plot(accel_time[5:], integrate.cumtrapz(accel_Y[5:], accel_time[5:], initial=0), 'tab:orange')
    axs[1, 1].set_title('speed Y')

    axs[2, 0].plot(accel_time[5:], accel_Z[5:], 'tab:green')
    axs[2, 0].set_title('accel Z')
    axs[2, 1].plot(accel_time[5:], integrate.cumtrapz(accel_Z[5:], accel_time[5:], initial=0), 'tab:green')
    axs[2, 1].set_title('speed Z')
    plt.show()

run()