#! /usr/bin/env python3

# Author:       Arturo Aguilar Lagunas
# Date:         Tue Oct 19 12:17:43 PM CDT 2021
# Description:  Main file for testing

from rlib import Axis, Link, Mecha
from matplotlib.animation import FuncAnimation
from pynput import keyboard
import matplotlib.pyplot as plt
import numpy as np
import threading

# TODO: CREATE MODULE FOR GRAPHING WITH MATPLOTLIB
# TODO: CREATE MODULE FOR GRAPHING WITH OPENGL

# variables
dh = [
    [0, 0, 0, 0],
    [9, 0, 0, 0],
    [9, 0, 0, 0],
    [0, 0, 8, 0]
]
mecha = Mecha(dh_args=dh)
current_link = 0
step = np.pi/8

# pynput, keyboard handler

def on_press(key):
    global current_link, mecha
    try:
        k = key.char
        if k in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if int(k) < len(mecha.links):
                print('link-{} -> link-{}'.format(mecha.links[current_link].id, k))
                current_link = int(k)
            else:
                print('link does not exists')
        elif k == 'x':
            mecha.rotate(current_link, alpha=step)
        elif k == 'X':
            mecha.rotate(current_link, alpha=-step)
            pass
        elif k == 'y':
            mecha.rotate(current_link, beta=step)
            pass
        elif k == 'Y':
            mecha.rotate(current_link, beta=-step)
            pass
        elif k == 'z':
            mecha.rotate(current_link, gamma=step)
            pass
        elif k == 'Z':
            mecha.rotate(current_link, gamma=-step)
        else:
            pass
    except AttributeError:
        pass
        # print('special key {0} pressed'.format(key))

'''
def on_press(key):
    global current_link, mecha
    try:
        k = key.char
        if k in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if int(k) < len(mecha.links):
                print('link-{} -> link-{}'.format(mecha.links[current_link].id, k))
                current_link = int(k)
            else:
                print('link does not exists')
        elif k == 'x':
            mecha.links[current_link].rotate(alpha=step)
        elif k == 'X':
            mecha.links[current_link].rotate(alpha=-step)
            pass
        elif k == 'y':
            mecha.links[current_link].rotate(beta=step)
            pass
        elif k == 'Y':
            mecha.links[current_link].rotate(beta=-step)
            pass
        elif k == 'z':
            mecha.links[current_link].rotate(gamma=step)
            pass
        elif k == 'Z':
            mecha.links[current_link].rotate(gamma=-step)
        else:
            pass
    except AttributeError:
        pass
        # print('special key {0} pressed'.format(key))
'''
listener = keyboard.Listener(on_press=on_press)
listener.start()

# matplotlib, plotting
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
    space = 3

    ax.cla()

    ax.axes.set_xlim3d(right=space, left=-space)
    ax.axes.set_ylim3d(bottom=space, top=-space)
    ax.axes.set_zlim3d(bottom=-space, top=space)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # plot_axis(origin)
    for arm in mecha.links: plot_element(arm)

ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.show()
