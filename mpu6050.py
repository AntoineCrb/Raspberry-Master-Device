import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from mpu6050 import mpu6050
import time

plt.style.use('ggplot')

def live_plotter(x_vec,y1_data,line1,pause_time,identifier=''):
    if line1==[]:
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    line1.set_ydata(y1_data)
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    plt.pause(pause_time)
    return line1

mpu = mpu6050(0x68)
coord = ['x', 'y', 'z']
offs = [0, 0, 0]
speed = [0, 0, 0]

def init():
    print("--- initialisation")
    mpu.set_accel_range(mpu.ACCEL_RANGE_2G)
    mpu.set_gyro_range(mpu.GYRO_RANGE_250DEG)
    reset_offset()

def reset_offset():
    global offs
    print("--- offset loading...")
    data = get_accel(100,0.01)
    offs = [data[k] for k in coord]
    print("--- offset calculated : " + str(offs))

def get_accel(n, t):
    o = {'x':0,'y':0,'z':0}
    for _ in range(n):
        ac_data = mpu.get_accel_data()
        for k in coord:
            o[k] += ac_data[k]
        time.sleep(t)
    return {'x':o['x']/n-offs[0], 'y':o['y']/n-offs[1], 'z':o['z']/n-offs[2]}

def set_speed(current_acc, delta_time):
    for k in range(len(coord)):
        speed[k] += current_acc[coord[k]]*delta_time

def save_data(s_file, accel):
    s_file.write('speed : ' )
    s_file.write(str(speed))
    s_file.write('acc : ')
    s_file.write(str(accel) + '\n')

def run():
    now = str(datetime.now())
    save_file = open("data_mpu_" + now + ".txt", "x")
    size = 100
    x_vec = np.linspace(0,1,size+1)[0:-1]
    y_vec = np.zeros(len(x_vec))
    line1 = []
    init()
    while True:
        data = get_accel(3, 0.005)
        set_speed(data,0.03)
        s = ""
        for k in coord:
            s += k + ': ' +  ("" if data[k] < 0 else " ") + str("%.1f" % data[k]) + ' - '
        save_data(save_file, s)
        print(s)
        y_vec[-1] = "%.1f" % data['z']
        line1 = live_plotter(x_vec,y_vec,line1, 0.015, identifier="Z accel")
        y_vec = np.append(y_vec[1:],0.0)

run()
