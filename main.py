#! /usr/bin/env python3

# Author:		Arturo Aguilar Lagunas
# Date:			Tue Oct 19 12:17:43 PM CDT 2021
# Description:	Main file for testing

from stuff import Axis
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import threading

origin = Axis(0, 0, 0)
arm1 = Axis(0, 0, 0)
amt = np.pi/10

def key_listening():
    global arm1, amt
    while True:
        command = input('Command: ')
        if command == 'x':
            arm1.rotate(alpha=amt)
        elif command == 'y':
            arm1.rotate(beta=amt)
        elif command == 'z':
            arm1.rotate(gamma=amt)
        elif command == '-x':
            arm1.rotate(alpha=-amt)
        elif command == '-y':
            arm1.rotate(beta=-amt)
        elif command == '-z':
            arm1.rotate(gamma=-amt)
        else:
            print('Invalid command')

t_keys = threading.Thread(target=key_listening, args=())
t_keys.start()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def plotAxis(a):
    start_pos = a.p.flatten()
    ax.scatter(start_pos[0], start_pos[1], start_pos[2], marker='o')
    for end_pos in a.axises:
        ax.plot(
            [start_pos[0], start_pos[0] + end_pos[0]],
            [start_pos[1], start_pos[1] + end_pos[1]],
            [start_pos[2], start_pos[2] + end_pos[2]])

def animate(i):
    global sx_data, sy_data, sz_data
    ax.cla()

    ax.axes.set_xlim3d(right=3, left=-3)
    ax.axes.set_ylim3d(bottom=3, top=-3)
    ax.axes.set_zlim3d(bottom=-3, top=3)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plotAxis(origin)
    plotAxis(arm1)


ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.show()

