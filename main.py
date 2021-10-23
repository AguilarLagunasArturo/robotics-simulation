#! /usr/bin/env python3

# Author:       Arturo Aguilar Lagunas
# Date:         Tue Oct 19 12:17:43 PM CDT 2021
# Description:  Main file for testing

from rlib import Axis, Link
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import threading

# TODO: CREATE MODULE FOR GRAPHING WITH MATPLOTLIB
# TODO: CREATE MODULE FOR GRAPHING WITH OPENGL

# TODO: COMPARE AXISES/LINKS SPAWNED W/ THE SAME ANGLES BUT IN DIFFERENT ORDER
origin = Axis()
# arm1 = Link(pos=[0, 0, 0], dir=[np.pi/50, np.pi/50, 0.0],mag=1.0)
arm1 = Link(pos=[0, 0, 0], mag=2.0)
arm2 = Link(pos=[0, 0, 2], mag=0.5)

amt = np.pi/8

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

def plot_axis(a):
    colors = ['c', 'g', 'm']
    start_pos = a.pos.flatten()
    ax.scatter(start_pos[0], start_pos[1], start_pos[2], marker='o')
    for i, end_pos in enumerate( a.axises ):
        ax.plot(
            [start_pos[0], start_pos[0] + end_pos[0]],
            [start_pos[1], start_pos[1] + end_pos[1]],
            [start_pos[2], start_pos[2] + end_pos[2]], color=colors[i%3])

def plot_link(l):
    start_pos = l.pos.flatten()
    end_pos = l.vec.flatten()
    ax.plot(
        [start_pos[0], start_pos[0] + end_pos[0]],
        [start_pos[1], start_pos[1] + end_pos[1]],
        [start_pos[2], start_pos[2] + end_pos[2]])

def plot_element(e):
    plot_axis(e.axis)
    plot_link(e)

def animate(i):
    global origin, arm1
    ax.cla()

    ax.axes.set_xlim3d(right=3, left=-3)
    ax.axes.set_ylim3d(bottom=3, top=-3)
    ax.axes.set_zlim3d(bottom=-3, top=3)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # plot_axis(origin)
    plot_element(arm1)
    plot_element(arm2)

ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.show()
